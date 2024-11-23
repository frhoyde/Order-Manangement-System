from rest_framework import serializers
from models.state import Event
from serializers.state_serializer import StateSerializer
from apps.orders.serializers.order_serializer import Order

class EventSerializer(serializers.ModelSerializer):
    sources = StateSerializer(many=True, read_only=True)
    destinations = StateSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'name', 'sources', 'destinations', 'order_type_id']