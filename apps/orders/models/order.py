from django.db import models
from django.conf import settings
from apps.products.models.product import Product
from statemachine.mixins import MachineMixin
from apps.states.services.state_service import StateService
from apps.states.models.state import Event
from pathlib import Path


class OrderType(models.Model):
    customer_type = models.CharField(max_length=100)
    service_type = models.CharField(max_length=100)

    event = models.OneToOneField(
        Event,
        
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = (('customer_type', 'service_type'))

class  Order(models.Model, MachineMixin):
    state_machine_attr = 'sm'
    state_field_name = 'status'
    state_machine_name = 'StateService'
    status = models.CharField(max_length=100)
    total_amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    orderType = models.OneToOneField(OrderType, related_name='order', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_item_product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()



