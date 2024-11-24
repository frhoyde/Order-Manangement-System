from typing import Optional, List
from ..models.state import State, Event
from django.db import transaction
from apps.orders.models.order import OrderType

class EventRepository:
    def create_event(self, 
                name: str, 
                sources: List[State], 
                destinations: List[State],
                order_type: OrderType) -> Event:
        with transaction.atomic():
            event = Event.objects.create(
                name=name,
                orderType=order_type
            )
            event.sources.set(sources)
            event.destinations.set(destinations)
            return event
    
    def get_all_events(self):
        return Event.objects.all()

    def get_event_by_id(self, event_id: int) -> Optional[Event]:
        return Event.objects.filter(id=event_id).first()
    
    def get_events_by_order_type(self, order_type_id: int) -> List[Event]:
            return Event.objects.filter(orderType_id=order_type_id)
