from django import forms
from .models import Habit  # Import the correct model

class HabitForm(forms.ModelForm):  # Renamed to HabitForm
    class Meta:
        model = Habit  # Use the Habit model
        fields = ['name', 'description', 'category', 'completed']  # Removed 'created_at' as it is non-editable

        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
    