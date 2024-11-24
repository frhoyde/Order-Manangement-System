from statemachine import State, StateMachine, Event

class StateMachineService(StateMachine):
    def __init__(self, model=None, state_field='status', *args, **kwargs):
        from apps.states.repositories.state_repository import StateRepository
        from apps.states.services.event_service import EventService
        
        self.model = model
        self.state_field = state_field
        self.state_repository = StateRepository()
        self.event_service = EventService()
        
        # Get all states and events before initializing
        self.states = {}
        self._events = {}
        
        # Load states from database
        existing_states = self.state_repository.get_all_states()
        for state in existing_states:
            self.states[state.id] = State(
                name=state.name,
                value=state.id,  # Use ID as the value
                initial=state.is_initial,
                final=state.is_final
            )
        
        # Load transitions and events from database
        existing_events = self.event_service.get_all_events()
        for event in existing_events:
            transitions = []
            # Create transitions for each source-destination pair
            for source, destination in zip(event['sources'], event['destinations']):
                if source in self.states and destination in self.states:
                    transitions.append(
                        self.states[source].to(self.states[destination])
                    )
            
            if transitions:
                # Create the event with its transitions
                self._events[event['id']] = Event(
                    name=event['name'],
                    value=event['id'],
                    transitions=transitions
                )
        
    
    @property
    def events(self):
        return self._events
    
    def get_state_value(self, state_id):
        """Get the actual value for a state"""
        return self.states[state_id].value if state_id in self.states else None
    
    def can_transition(self, event_id):
        """Check if a transition is possible"""
        event = self._events.get(event_id)
        if event:
            return event.can_run(self)
        return False
    
    def trigger_event(self, event_id):
        """Trigger a specific event by ID"""
        event = self._events.get(event_id)
        if event:
            if event.can_run(self):
                event.run(self)
                return True
        return False