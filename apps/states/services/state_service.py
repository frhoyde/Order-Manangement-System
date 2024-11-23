from statemachine import StateMachine
from statemachine import State, Event
from ..repositories.state_repository import StateRepository
from ..serializers.state_serializer import StateSerializer

class StateService():
    def __init__(self) -> None:
        self.repository = StateRepository()

        states = dict()
        existing_states = self.repository.get_all_states()

        for i in existing_states:
            states[i.id] = State(i.name, i.id, initial=i.is_initial, final=i.is_final)
        
        events = dict()

        transitions = list()

        existing_events = self.repository.get_all_events()
        
        for event in existing_events:
            sources = event.sources
            destinations = event.destinations
            for source, index in enumerate(sources):
                transitions.append(source.to(destinations[index]))
            

            events[event.name] = transitions
            transitions.clear()


    def create_state(self, state_data):
        state = self.repository.create_state(state_data)
        serializer = StateSerializer(state)
        return serializer.data
    
    def get_states(self):
        states = self.repository.get_all_states()
        serializer = StateSerializer(states, many=True)
        return serializer.data

    def delete_state(self, state_id):
        state = self.repository.delete_state(state_id)
        serializer = StateSerializer(state)
        return serializer.data

    
