from django.db import models
from django.conf import settings
from apps.products.models.product import Product
from apps.orders.models.order import OrderType
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

    orderType = models.ForeignKey(OrderType, related_name='events', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
    
class  State(models.Model):
    name = models.CharField(max_length=100, unique=True)

    is_initial = models.BooleanField(default=False)
    is_final = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']


    

