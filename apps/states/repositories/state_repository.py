from typing import Optional
from ..models.state import State

class StateRepository:
    def create_state(self, state_data: dict) -> State:
        state = State.objects.create(
            name = state_data['name'],
            value = state_data['value'],
            is_initial = state_data['initial'],
            is_final = state_data['final']
        )

        return state
    

