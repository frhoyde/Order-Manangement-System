from rest_framework import serializers
from ..serializers.state_serializer import StateSerializer
from ..models.state import Event, State
from apps.orders.models.order import OrderType

class EventSerializer(serializers.ModelSerializer):

    sources = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=State.objects.all()
    )
    destinations = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=State.objects.all()
    )

    class Meta:
        model = Event
        fields = ['id', 'name', 'sources', 'destinations', 'orderType_id']


class EventCreateSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    sources = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=State.objects.all()
    )
    destinations = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=State.objects.all()
    )
    orderType = serializers.PrimaryKeyRelatedField(queryset=OrderType.objects.all())

    class Meta:
        model = Event
        fields = ['name', 'sources', 'destinations', 'orderType']

    def validate(self, data):
        if not data['sources']:
            raise serializers.ValidationError("At least one source state is required")
        if not data['destinations']:
            raise serializers.ValidationError("At least one destination state is required")
        return data