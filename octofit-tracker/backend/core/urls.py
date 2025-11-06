from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActivityViewSet, UserProfileViewSet

router = DefaultRouter()
router.register(r'activities', ActivityViewSet)
router.register(r'profiles', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
