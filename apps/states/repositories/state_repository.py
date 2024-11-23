from typing import Optional
from ..models.state import State
from ..models.state import Event

class StateRepository:
    def create_state(self, state_data: dict) -> State:
        state = State.objects.create(
            name = state_data['name'],
            value = state_data['value'],
            is_initial = state_data['is_initial'],
            is_final = state_data['is_final']
        )

        return state
    
    def get_all_states(self):
        return State.objects.all()
    
    def get_state_by_value(self):
        pass

    def get_all_events(self):
        return Event.objects.all()