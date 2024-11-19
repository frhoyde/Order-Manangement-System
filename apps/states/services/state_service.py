from statemachine import StateMachine
from statemachine import State
from ..repositories.state_repository import StateRepository
from ..serializers.state_serializer import StateSerializer

class StateService():
    def __init__(self) -> None:
        self.repository = StateRepository()
        

    def create_state(self, state_data):
        state = self.repository.create_state(state_data)
        serializer = StateSerializer(state)
        return serializer.data

    def delete_state(self, state_id):
        pass

    
