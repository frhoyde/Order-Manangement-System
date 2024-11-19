from django.db import models
from django.conf import settings
from apps.products.models.product import Product

class  Event(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
    
class  State(models.Model):
    name = models.CharField(max_length=100, unique=True)
    value = models.IntegerField(serialize=True ,unique=True)

    is_initial = models.BooleanField(default=False)
    is_final = models.BooleanField(default=False)
    event = models.ForeignKey(Event, related_name='sources', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name='destinations', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.source} -> {self.dest}"
    
    class Meta:
        ordering = ['value']


    

