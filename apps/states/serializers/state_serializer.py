from rest_framework import serializers
from ..models.state import State

class StateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = State
        fields = ['id', 'name', 'value', 'is_initial', 'is_final']