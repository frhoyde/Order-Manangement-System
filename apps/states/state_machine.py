from statemachine import State, StateMachine, Event
from statemachine.transition_list import TransitionList
from .services.state_service import StateService
from .services.event_service import EventService

class StateMachineService(StateMachine):

######################### Testing Purposes Only#########################
    # red = State('Red', initial=True)
    # green = State('Green')
    # yellow = State('Yellow')
    # go = red.to(green) | green.to(yellow)
######################### Testing Purposes Only#########################
    state_service = StateService()
    event_service = EventService()

    existing_states = state_service.get_states()
    allow_empty_transitions = True

    # dict of state names with their values as keys
    state_names = {state['id']: state['name'].lower().replace(' ', '_') for state in existing_states}


    # Define states for the state machine
    for state in existing_states:
        locals()[f"{state['name'].lower().replace(' ', '_')}"] = State(name=state['name'], value=state['id'], initial=state['is_initial'], final=state['is_final'])
    

    existing_events = event_service.get_available_events(order_type_id=1)
    for event in existing_events:
        transitions = TransitionList()
        for source, destination in zip(event['sources'], event['destinations']):
            transitions.add_transitions(locals()[f"{state_names[source]}"].to(locals()[f"{state_names[destination]}"]))
        locals()[event['name']] = Event(transitions=transitions, id=event['name'], name=event['name'], _sm=locals())



    # def __init__(self, model=None, state_field='status', *args, **kwargs):
        
    #     self.model = model
    #     self.state_field = state_field
    #     self.state_repository = StateRepository()
    #     self.event_service = EventService()
        
    #     # Load states from database
    #     for state in existing_states:
    #         x = self.__class__.add_state("_".join(state.name.lower().split(' ')), State(
    #             name=state.name,
    #             value=state.id,  
    #             initial=state.is_initial,
    #             final=state.is_final
    #         ))
        
        
    #     state_attributes = [s.id for s in self.__class__.states]
    #     existing_events = self.event_service.get_all_events()

    #     for event in existing_events:
    #         transitions = TransitionList()
    #         for source, destination in zip(event['sources'], event['destinations']):
    #                 transitions.add_transitions(self.__class__.states.__getattr__(state_attributes[source - 1]).to(self.__class__.states.__getattr__(state_attributes[destination - 1])))
            
    #         self.__class__.add_event(event=Event(
    #             transitions=transitions,
    #             name=event['name'],
    #             id=event['name'],
    #             _sm=self
    #         ))


    def before_flow(self, event: str, source: State, target: State):
        print(f"Running {event} from {source.id} to {target.id}")

                
            