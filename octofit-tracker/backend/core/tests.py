from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from .models import UserProfile, Activity


class HealthEndpointTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_health_ok(self):
        resp = self.client.get('/api/health/')
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(data.get('status'), 'ok')


class ModelsTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='tester', password='pwd')

    def test_profile_and_activity(self):
        profile = UserProfile.objects.create(user=self.user, bio='hello')
        act = Activity.objects.create(user=self.user, activity_type='run', duration_minutes=30)
        self.assertEqual(str(profile), f'Profile for {self.user.username}')
        self.assertIn('run', str(act))
