from django.db import models
from django.conf import settings

class  Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'PENDING'),
        ('paid', "PAID"),
        ('shipped', 'SHIPPED'),
        ('delivered', 'DELIVERED'),
        ('cancelled', 'CANCELLED'),
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)



