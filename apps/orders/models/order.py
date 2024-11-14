from django.db import models
from django.conf import settings
from apps.products.models.product import Product
from statemachine.mixins import MachineMixin
from apps.states.services.state_service import StateService
from pathlib import Path


class  Order(models.Model, MachineMixin):
    state_machine_attr = 'sm'
    state_field_name = 'status'
    state_machine_name = 'StateService'
    status = models.CharField(max_length=100)
    total_amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_item_product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()



