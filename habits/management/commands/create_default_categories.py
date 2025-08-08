from django.core.management.base import BaseCommand
from habits.models import Category


class Command(BaseCommand):
    help = 'Create default categories for the habit tracker'

    def handle(self, *args, **options):
        # Default categories to create
        default_categories = [
            'Health & Fitness',
            'Learning & Education',
            'Productivity',
            'Personal Development',
            'Social & Relationships',
            'Hobbies & Creativity',
            'Finance & Career',
            'Mindfulness & Wellness'
        ]

        created_count = 0
        for category_name in default_categories:
            category, created = Category.objects.get_or_create(
                name=category_name
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Created category: {category_name}'
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f'Category already exists: {category_name}'
                    )
                )

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created {created_count} new categories!'
            )
        )