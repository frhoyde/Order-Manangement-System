from apps.states.repositories.state_repository import StateRepository
from apps.states.constants.states import StateConstants 
class StateSeeder:
    def __init__(self) -> None:
        self.state_repository = StateRepository()
        self.constants = StateConstants()

        existing_states = self.state_repository.get_all_states()

        if len(existing_states) == 0:
            print('Seeding States')
            for el in self.constants.default_states:
                obj = self.state_repository.create_state({**el})
                print(f'name: {obj.name}, value: {obj.id}, initial: {obj.is_initial}, final: {obj.is_final}')

        else:
            print(f'States already Exist! Count: {len(existing_states)}')
            for obj in existing_states:
                print(f'{obj.id} - name: {obj.name}, value: {obj.id}, initial: {obj.is_initial}, final: {obj.is_final}')