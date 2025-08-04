from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime, timedelta

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Unique category name

    def __str__(self):
        return self.name  # String representation of the category


class Habit(models.Model):
    name = models.CharField(max_length=100)  # Name of the habit
    description = models.TextField(blank=True, null=True)  # Optional description
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when created
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Link to Category
    completed = models.BooleanField(default=False)  # Whether the habit is completed
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User

    def __str__(self):
        return self.name  # String representation of the habit


class Progress(models.Model):
    date = models.DateField()  # Date of the progress entry
    status = models.BooleanField(default=False)  # Whether the habit was completed
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)  # Link to Habit

    def __str__(self):
        return f"{self.habit.name} - {self.date} - {'Completed' if self.status else 'Not Completed'}"


class PasswordResetToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)
    
    def is_valid(self):
        """Check if token is still valid (24 hours)"""
        expiry_time = self.created_at + timedelta(hours=24)
        return not self.is_used and datetime.now().replace(tzinfo=None) < expiry_time.replace(tzinfo=None)
    
    def mark_as_used(self):
        """Mark token as used"""
        self.is_used = True
        self.save()
    
    def __str__(self):
        return f"Password reset token for {self.user.username}"