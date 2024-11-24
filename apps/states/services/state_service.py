from statemachine import StateMachine
from statemachine import State, Event
from ..repositories.state_repository import StateRepository
from ..services.event_service import EventService
from ..serializers.state_serializer import StateSerializer

class StateService():
    def __init__(self) -> None:
        self.state_repository = StateRepository()
        self.event_service = EventService()

        # states = dict()
        # existing_states = self.state_repository.get_all_states()

        # for i in existing_states:
        #     states[i.id] = State(i.name, i.id, initial=i.is_initial, final=i.is_final)

        # self.events = dict()

        # transitions = list()

        # existing_events = self.event_service.get_all_events()

        # for event in existing_events:
        #     for idx, source in enumerate(event['sources']):
        #         transitions.append(states[source].to(states[event['destinations'][idx]]))
            

        #     self.events[event['id']] = Event(transitions=transitions, name=event['name'], id=event['id'])
        #     print(self.events[event['id']])
        

    def create_state(self, state_data):
        state = self.state_repository.create_state(state_data)
        serializer = StateSerializer(state)
        return serializer.data
    
    def get_states(self):
        states = self.state_repository.get_all_states()
        serializer = StateSerializer(states, many=True)
        return serializer.data

    def delete_state(self, state_id):
        state = self.repository.delete_state(state_id)
        serializer = StateSerializer(state)
        return serializer.data

    
