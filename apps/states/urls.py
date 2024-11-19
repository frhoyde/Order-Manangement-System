from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .apis.state_api import StateViewSet

router = DefaultRouter()
router.register(r'', StateViewSet, basename='')

urlpatterns = [
    path('', include(router.urls)),
]
