from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .apis.order_api import OrderViewSet

router = DefaultRouter()
router.register(r'', OrderViewSet, basename='')

urlpatterns = [
    path('', include(router.urls)),
]
