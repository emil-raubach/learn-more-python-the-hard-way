# Just going to straight copy Zed's implementation since I really 
# just feel stuck / not sure how to move forward.  
from inspect import getmembers
import re

STATE_NAME = re.compile('^[A-Z0-9]+$')

class FSM(object):
    """Class to implement a basic Finite State Machine"""
    def __init__(self):
        self.state_name = 'START'
        members = getmembers(self)
        self.possible_states = {}

        for k, v in members:
            if STATE_NAME.match(k):
                self.possible_states[k] = v
    
    def handle(self, event):
        """Setter function to change the state of the FSM."""
        state_handler = self.lookup_state()
        self.state_name = state_handler(event)

    def lookup_state(self):
        return self.possible_states.get(self.state_name)