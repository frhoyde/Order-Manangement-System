from statemachine import State, StateMachine, Event
from statemachine.transition_list import TransitionList

class StateMachineService(StateMachine):
    def __init__(self, model=None, state_field='status', *args, **kwargs):
        from apps.states.repositories.state_repository import StateRepository
        from apps.states.services.event_service import EventService
        
        self.state_field = state_field
        self.state_repository = StateRepository()
        self.event_service = EventService()
        
        # Load states from database
        existing_states = self.state_repository.get_all_states()
        for state in existing_states:
            x = self.__class__.add_state("_".join(state.name.lower().split(' ')), State(
                name=state.name,
                value=state.id,  
                initial=state.is_initial,
                final=state.is_final
            ))
        
        
        state_attributes = [s.id for s in self.__class__.states]
        existing_events = self.event_service.get_all_events()

        for event in existing_events:
            transitions = TransitionList()
            for source, destination in zip(event['sources'], event['destinations']):
                    transitions.add_transitions(self.__class__.states.__getattr__(state_attributes[source - 1]).to(self.__class__.states.__getattr__(state_attributes[destination - 1])))
            
            self.__class__.add_event(event=Event(
                transitions=transitions,
                name=event['name'],
                id=event['name'],
                _sm=self
            ))
        print(StateMachineService.flow)

                
            
        
    
    def trigger_event(self, event_id):
        """Trigger a specific event by ID"""
        print(StateMachineService.events)