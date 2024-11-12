from django.db import models
from django.conf import settings
from apps.products.models.product import Product

class  Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'PENDING'),
        ('paid', "PAID"),
        ('shipped', 'SHIPPED'),
        ('delivered', 'DELIVERED'),
        ('cancelled', 'CANCELLED'),
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_item_product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()



