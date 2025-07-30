# filepath: /Users/shellie/project/habit-tracker/habits/views.py
from django.shortcuts import render

def my_habit(request):
    return render(request, 'habits/home.html')  # Render a template