from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.http import Http404, JsonResponse
from .models import Habit, PasswordResetToken
from .forms import HabitForm
from .auth_forms import CustomUserCreationForm, CustomAuthenticationForm, CustomPasswordResetForm, PasswordResetConfirmForm
import uuid
from datetime import datetime

@login_required
def my_habit(request):
    """
    A view to display habits to do and completed habits
    with the habits due soonest at the top.
    """
    to_do_habits = Habit.objects.filter(completed=False, user=request.user).order_by('created_at')
    done_habits = Habit.objects.filter(completed=True, user=request.user).order_by('created_at')

    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            
            # Enhanced notification for habit creation
            messages.success(
                request, 
                f'🎉 Great job! Habit "{habit.name}" has been added to your tracker!',
                extra_tags='habit-added'
            )
            
            # Store notification data in session for browser notification
            request.session['notification'] = {
                'type': 'success',
                'title': 'New Habit Added!',
                'message': f'"{habit.name}" is now being tracked',
                'icon': '🎯'
            }
            
            return redirect('home')
    else:
        form = HabitForm()

    context = {
        'to_do_habits': to_do_habits,
        'done_habits': done_habits,
        'form': form,
    }

    return render(request, 'habits/index.html', context)

def signup_view(request):
    """User registration view"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'habits/auth/signup.html', {'form': form})

def login_view(request):
    """User login view"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.first_name}!')
                next_url = request.GET.get('next', 'home')
                return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'habits/auth/login.html', {'form': form})

def logout_view(request):
    """User logout view"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

def password_reset_request_view(request):
    """Password reset request view"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                
                # Create password reset token
                reset_token = PasswordResetToken.objects.create(user=user)
                
                # Create reset URL
                reset_url = request.build_absolute_uri(
                    reverse('password_reset_confirm', kwargs={'token': reset_token.token})
                )
                
                # Send email (in production, you'd use a proper email backend)
                subject = 'Password Reset - Habit Tracker'
                message = f'''
Hello {user.first_name},

You requested a password reset for your Habit Tracker account.
Click the link below to reset your password:

{reset_url}

This link will expire in 24 hours.

If you didn't request this, please ignore this email.

Best regards,
Habit Tracker Team
                '''
                
                try:
                    send_mail(
                        subject,
                        message,
                        settings.DEFAULT_FROM_EMAIL,
                        [email],
                        fail_silently=False,
                    )
                    messages.success(request, 'Password reset email sent! Check your inbox.')
                except Exception as e:
                    # For development, show the reset link directly
                    messages.success(request, f'Password reset link (for development): {reset_url}')
                
                return redirect('password_reset_done')
                
            except User.DoesNotExist:
                # Don't reveal if email exists or not for security
                messages.success(request, 'If an account with that email exists, a password reset link has been sent.')
                return redirect('password_reset_done')
    else:
        form = CustomPasswordResetForm()
    
    return render(request, 'habits/auth/password_reset.html', {'form': form})

def password_reset_done_view(request):
    """Password reset email sent confirmation"""
    return render(request, 'habits/auth/password_reset_done.html')

def password_reset_confirm_view(request, token):
    """Password reset confirmation view"""
    try:
        reset_token = get_object_or_404(PasswordResetToken, token=token)
        
        if not reset_token.is_valid():
            messages.error(request, 'This password reset link has expired or is invalid.')
            return redirect('password_reset_request')
        
        if request.method == 'POST':
            form = PasswordResetConfirmForm(request.POST)
            if form.is_valid():
                new_password = form.cleaned_data['new_password1']
                user = reset_token.user
                user.set_password(new_password)
                user.save()
                
                # Mark token as used
                reset_token.mark_as_used()
                
                messages.success(request, 'Your password has been reset successfully! You can now log in.')
                return redirect('login')
        else:
            form = PasswordResetConfirmForm()
        
        return render(request, 'habits/auth/password_reset_confirm.html', {
            'form': form,
            'token': token
        })
        
    except Exception:
        raise Http404("Invalid password reset link")

def password_reset_complete_view(request):
    """Password reset complete confirmation"""
    return render(request, 'habits/auth/password_reset_complete.html')

@login_required
def edit_habit(request, habit_id):
    """
    Edit an existing habit
    """
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    original_name = habit.name
    
    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            updated_habit = form.save()
            
            # Enhanced notification for habit editing
            messages.success(
                request, 
                f'✏️ Habit "{updated_habit.name}" has been updated successfully!',
                extra_tags='habit-edited'
            )
            
            # Store notification data in session for browser notification
            request.session['notification'] = {
                'type': 'info',
                'title': 'Habit Updated!',
                'message': f'Changes to "{updated_habit.name}" have been saved',
                'icon': '✏️'
            }
            
            return redirect('home')
    else:
        form = HabitForm(instance=habit)
    
    context = {
        'form': form,
        'habit': habit,
    }
    
    return render(request, 'habits/edit_habit.html', context)

@login_required
def delete_habit(request, habit_id):
    """
    Delete an existing habit
    """
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    
    if request.method == 'POST':
        habit_name = habit.name
        habit.delete()
        
        # Enhanced notification for habit deletion
        messages.warning(
            request, 
            f'🗑️ Habit "{habit_name}" has been deleted from your tracker.',
            extra_tags='habit-deleted'
        )
        
        # Store notification data in session for browser notification
        request.session['notification'] = {
            'type': 'warning',
            'title': 'Habit Deleted',
            'message': f'"{habit_name}" has been removed from your tracker',
            'icon': '🗑️'
        }
        
        return redirect('home')
    
    context = {
        'habit': habit,
    }
    
    return render(request, 'habits/delete_habit.html', context)

@login_required
def toggle_habit_completion(request, habit_id):
    """
    Toggle habit completion status
    """
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    
    habit.completed = not habit.completed
    habit.save()
    
    if habit.completed:
        # Celebration notification for completion
        messages.success(
            request, 
            f'🎉 Congratulations! You completed "{habit.name}"! Keep up the great work!',
            extra_tags='habit-completed'
        )
        
        # Store celebration notification for browser
        request.session['notification'] = {
            'type': 'celebration',
            'title': 'Habit Completed! 🎉',
            'message': f'Amazing work on "{habit.name}"!',
            'icon': '🏆'
        }
    else:
        # Notification for marking as pending
        messages.info(
            request, 
            f'📝 Habit "{habit.name}" has been marked as pending.',
            extra_tags='habit-pending'
        )
        
        # Store notification for browser
        request.session['notification'] = {
            'type': 'info',
            'title': 'Habit Status Changed',
            'message': f'"{habit.name}" is now pending',
            'icon': '📝'
        }
    
    return redirect('home')

@login_required
def get_notification(request):
    """
    API endpoint to get notification data for browser notifications
    """
    notification = request.session.pop('notification', None)
    if notification:
        return JsonResponse(notification)
    return JsonResponse({})

@login_required
def mark_habit_completed_ajax(request, habit_id):
    """
    AJAX endpoint for completing habits with instant notifications
    """
    if request.method == 'POST':
        habit = get_object_or_404(Habit, id=habit_id, user=request.user)
        habit.completed = True
        habit.save()
        
        return JsonResponse({
            'success': True,
            'message': f'🎉 Congratulations! You completed "{habit.name}"!',
            'habit_name': habit.name,
            'notification': {
                'type': 'celebration',
                'title': 'Habit Completed! 🎉',
                'message': f'Amazing work on "{habit.name}"!',
                'icon': '🏆'
            }
        })
    
    return JsonResponse({'success': False})