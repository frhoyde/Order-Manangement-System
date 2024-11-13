from statemachine import StateMachine
from statemachine import State

class StateService(StateMachine):
    pending = State('Pending', initial=True, value="pending")
    paid = State('Paid', value="paid")
    shipped = State('Shipped', value="shipped")
    delivered = State('Delivered', value="delivered", final=True)
    cancelled = State('Cancelled', value="cancelled", final=True)

    flow = pending.to(paid) | paid.to(shipped) | shipped.to(delivered)
    any_to_cancel = cancelled.from_(pending, paid, shipped)

    def before_transition(self, event, state):

        print(f"Before '{event}', on the '{state.id}' state.")

        return "before_transition_return"


    def on_transition(self, event, state):

        print(f"On '{event}', on the '{state.id}' state.")

        return "on_transition_return"


    def on_exit_state(self, event, state):

        print(f"Exiting '{state.id}' state from '{event}' event.")


    def on_enter_state(self, event, state):

        print(f"Entering '{state.id}' state from '{event}' event.")


    def after_transition(self, event, state):

        print(f"After '{event}', on the '{state.id}' state.")