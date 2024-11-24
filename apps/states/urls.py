from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .apis.state_api import StateViewSet
from .apis.event_api import EventViewSet

router = DefaultRouter()
router.register(r'', StateViewSet, basename='')
router.register(r'event', EventViewSet, basename='event')

urlpatterns = [
    path('', include(router.urls)),
]
