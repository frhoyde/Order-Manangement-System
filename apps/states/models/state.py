from django.db import models
from django.conf import settings
from apps.products.models.product import Product

class  State(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
    

