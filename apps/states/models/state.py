from django.db import models
from django.conf import settings
from apps.products.models.product import Product

class  State(models.Model):
    name = models.CharField(max_length=100, unique=True)
    value = models.IntegerField(serialize=True ,unique=True)

    is_initial = models.BooleanField(default=False)
    is_final = models.BooleanField(default=False)

    class Meta:
        ordering = ['value']
    

