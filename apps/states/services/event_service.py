from ..repositories.event_repository import EventRepository
from ..serializers.event_serializer import EventSerializer

class EventService():
    def __init__(self) -> None:
        self.repository = EventRepository()

    def create_event(self, event_data):
        state = self.repository.create_event(event_data)
        serializer =  EventSerializer(event_data)
        return serializer.data
    
    def get_events(self):
        states = self.repository.get_all_events()
        serializer = EventSerializer(states, many=True)
        return serializer.data


    
