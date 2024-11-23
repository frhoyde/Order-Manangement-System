from django.db import models
from django.conf import settings
from apps.products.models.product import Product
from statemachine.mixins import MachineMixin

class OrderType(models.Model):
    customer_type = models.CharField(max_length=100)
    service_type = models.CharField(max_length=100)
    
    class Meta:
        unique_together = (('customer_type', 'service_type'),)
        db_table = 'orders_ordertype'  # explicitly set table name
        
    def __str__(self):
        return f"{self.customer_type} - {self.service_type}"

class Order(models.Model, MachineMixin):
    state_machine_attr = 'sm'
    state_field_name = 'status'
    state_machine_name = 'StateService'
    
    status = models.CharField(max_length=100)
    total_amount = models.FloatField()
    order_type = models.ForeignKey(
        OrderType, 
        on_delete=models.PROTECT,
        related_name='orders',
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        db_table = 'orders_order'  # explicitly set table name
        
    def __str__(self):
        return f"Order {self.id} - {self.status}"

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, 
        related_name='items',  # changed from 'order' to 'items'
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, 
        related_name='order_items',  # changed from 'order_item_product'
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField()
    
    class Meta:
        db_table = 'orders_orderitem'  # explicitly set table name
        
    def __str__(self):
        return f"OrderItem {self.id} for Order {self.order.id}"