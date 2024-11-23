from typing import Optional
from ..models.state import State
from ..models.state import Event

class EventRepository:
    def create_event(self, event_data: dict[Event]) -> Event:
        event = Event.objects.create(
           name = event_data['name'],
           sources = event_data['sources'],
           destinations = event_data['destinations'],
           order_type = event_data['order_type']
        )

        return event 
    
    def get_all_events(self):
        return Event.objects.all()
    