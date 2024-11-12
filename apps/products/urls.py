from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .apis.product_api import ProductViewSet

router = DefaultRouter()
router.register(r'', ProductViewSet, basename='')

urlpatterns = [
    path('', include(router.urls)),
]
