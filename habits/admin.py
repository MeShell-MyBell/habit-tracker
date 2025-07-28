from django.contrib import admin
from .models import Category, Task  # Import the models correctly

# Register your models with the admin site
admin.site.register(Category)
admin.site.register(Task)