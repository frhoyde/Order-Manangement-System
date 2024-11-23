from django.db import models
from django.conf import settings
from apps.products.models.product import Product

class  Event(models.Model):
    name = models.CharField(max_length=100)

    sources = models.ManyToManyField(
        'State', 
        related_name='events_as_source',
        related_query_name='event_source'
    )
    
    destinations = models.ManyToManyField(
        'State', 
        related_name='events_as_destination',
        related_query_name='event_destination'
    )


    class Meta:
        ordering = ['name']
    
class  State(models.Model):
    name = models.CharField(max_length=100, unique=True)
    value = models.IntegerField(unique=True)

    is_initial = models.BooleanField(default=False)
    is_final = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['value']


    

