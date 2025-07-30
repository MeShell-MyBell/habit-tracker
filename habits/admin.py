from django.contrib import admin
from .models import Category, Habit, Progress

admin.site.register(Category)
admin.site.register(Habit)
admin.site.register(Progress)