from django.shortcuts import render, redirect
from .models import Habit
from .forms import HabitForm  # Assuming you have a form for Habit

def my_habit(request):
    """
    A view to display habits to do and completed habits
    with the habits due soonest at the top.
    """
    to_do_habits = Habit.objects.filter(completed=False).order_by('due_date')
    done_habits = Habit.objects.filter(completed=True).order_by('due_date')

    context = {
        'to_do_habits': to_do_habits,
        'done_habits': done_habits,
    }

    return render(request, 'habits/index.html', context)

def add_habit(request):
    """
    A view to handle adding a new habit.
    """
    if request.method == 'POST':
        form = HabitForm(request.POST)