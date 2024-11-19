from django.db import models
from django.conf import settings
from apps.products.models.product import Product
from apps.orders.models.order import OrderType
from apps.states.models.state import State

class  Transition(models.Model):
    orderType = models.ForeignKey(OrderType, related_name='order_type_transition', on_delete=models.CASCADE)
    source = models.ForeignKey(State, related_name='source state', on_delete=models.CASCADE)
    next = models.ForeignKey(State, related_name='next_state', on_delete=models.CASCADE)


    class Meta:
        ordering = ['name']
    

