import time
from threading import Event as ThreadingEvent
from threading import Thread

from statemachine import State
from statemachine import StateMachine

class StateAdapter:
    def __init__(self, sm: StateMachine, sm_event: str):
        self.sm = sm
        self.sm_event = sm_event
        self.stop_event = ThreadingEvent()

    def run(self):
        while not self.stop_event.is_set():
            self.sm.send(self.sm_event)
            self.stop_event.wait(0.1)

    def stop(self):
        self.stop_event.set()
