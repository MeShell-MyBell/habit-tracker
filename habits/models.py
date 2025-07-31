from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Unique category name

    def __str__(self):
        return self.name  # String representation of the category


class Habit(models.Model):
    name = models.CharField(max_length=100)  # Name of the habit
    description = models.TextField(blank=True, null=True)  # Optional description
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when created
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Link to Category

    def __str__(self):
        return self.name  # String representation of the habit


class Progress(models.Model):
    date = models.DateField()  # Date of the progress entry
    status = models.BooleanField(default=False)  # Whether the habit was completed
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)  # Link to Habit

    def __str__(self):
        return f"{self.habit.name} - {self.date} - {'Completed' if self.status else 'Not Completed'}"     return f"{self.habit.name} - {self.date} - {'Completed' if self.status else 'Not Completed'}"