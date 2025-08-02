from django.shortcuts import render, redirect
from .models import Habit
from .forms import HabitForm  # Assuming you have a form for Habit

def my_habit(request):
    """
    A view to display habits to do and completed habits
    with the habits due soonest at the top.
    """
    to_do_habits = Habit.objects.filter(completed=False).order_by('created_at')  # Updated to use 'created_at'
    done_habits = Habit.objects.filter(completed=True).order_by('created_at')  # Updated to use 'created_at'

    if request.method == 'POST':
        form = HabitForm(request.POST)  # Corrected from TaskForm to HabitForm
        if form.is_valid():
            form.save()
            return redirect('home')  # Ensure 'home' is a valid URL name
    else:
        form = HabitForm()

    context = {
        'to_do_habits': to_do_habits,
        'done_habits': done_habits,
        'form': form,  # Added the form to the context
    }

    return render(request, 'habits/index.html', context)