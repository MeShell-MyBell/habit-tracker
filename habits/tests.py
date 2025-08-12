from django.test import TestCase
from django.urls import reverse


class HabitViewTests(TestCase):
    def test_my_habit_view(self):
        # Simulate a request to the 'my_habit' view
        response = self.client.get(reverse('my_habit'))
        
        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Check that the response contains the expected text
        self.assertContains(response, "Habit Tracker")
