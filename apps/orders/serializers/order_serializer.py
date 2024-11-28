from rest_framework import serializers
from ..models.order import Order, OrderItem, OrderType

class OrderTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderType
        fields = ['id', 'customer_type', 'service_type']
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product_id', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    order_type = OrderTypeSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'status', 'total_amount', 'items', 'order_type', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class CreateOrderItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)

class CreateOrderSerializer(serializers.Serializer):
    items = CreateOrderItemSerializer(many=True)
    order_type_id = serializers.IntegerField()

class UpdateOrderSerializer(serializers.Serializer):
    event_id = serializers.IntegerField()

    class Meta:
        model = Order