from django.contrib import admin
from .models import UserProfile, Activity


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_type', 'user', 'duration_minutes', 'recorded_at')
    list_filter = ('activity_type', 'recorded_at')
