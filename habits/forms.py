from django import forms
from .models import Habit  # Import the correct model

class HabitForm(forms.ModelForm):  # Renamed to HabitForm
    class Meta:
        model = Habit  # Use the Habit model
        fields = ['name', 'description', 'created_at', 'catergory',]  # Update fields to match Habit model

        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }
        