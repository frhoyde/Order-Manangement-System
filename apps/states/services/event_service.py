from typing import Dict, List
from ..repositories.event_repository import EventRepository
from django.core.exceptions import ValidationError
from apps.states.serializers.event_serializer import EventCreateSerializer, EventSerializer
from apps.orders.models.order import OrderType
from apps.states.models.state import Event

class EventService():
    def __init__(self) -> None:
        self.event_repository = EventRepository()
    

    def create_event(self, event_data: dict) -> Event:
        
        event = self.event_repository.create_event(
            name=event_data['name'],
            sources=event_data['sources'],
            destinations=event_data['destinations'],
            order_type=event_data['orderType']
        )
        serializer = EventSerializer(event)
        return serializer.data

    def get_available_events(self, order_type_id: int) -> List[Event]:
        events = self.event_repository.get_events_by_order_type(
            order_type_id
        )
        serializer = EventSerializer(events, many=True)
        return serializer.data
    
    def get_all_events(self) -> List[Event]:
        events = self.event_repository.get_all_events()
        serializer = EventSerializer(events, many=True)
        return serializer.data
    
    def get_event(self, event_id: int) -> Event:
        event = self.event_repository.get_event_by_id(event_id)
        serializer = EventSerializer(event)
        return serializer.data