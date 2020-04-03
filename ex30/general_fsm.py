class State(object):
    """Base class for states in a finite state machine."""
    def __init__(self):
        self.name = ""
        self.inputs = []
        self.outputs = []

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.name!r}:{self.inputs!r}:{self.outputs!r})')

    def __str__(self):
        return f'{self.name}'


class FSM(object):
    """Finite State Machine to control generic FSMs."""
    def __init__(self):
        self.current_state = None
        self.states = {}

    def next_state(self, event):
        """Transitions from one state to the next based on input."""
        print(f"The current state is '{self.current_state}''")
        for state, obj in self.states.items():
            print("> The event is: ", event)
            print(f">> The state being compared is: '{state}' obj is '{repr(obj)}'")
            if event in obj.inputs and obj.name in self.current_state.outputs:
                print(">>> event", event, "obj.inputs", obj.inputs)
                self.current_state = obj
                print(f"THE STATE IS NOW: ", self.current_state)
                return
            else:
                continue

    def start(self, state):
        """Sets the starting state of the FSM"""
        self.current_state = state
