from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserProfile, Activity

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'bio')


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('id', 'user', 'activity_type', 'duration_minutes', 'recorded_at')
