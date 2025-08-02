from django import forms
from .models import Habit  # Import the correct model

class HabitForm(forms.ModelForm):  # Renamed to HabitForm
    class Meta:
        model = Habit  # Use the Habit model
        fields = ['name', 'description', 'category', 'completed']  # Removed 'created_at' as it is non-editable

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter habit name'}),
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Enter habit description'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
