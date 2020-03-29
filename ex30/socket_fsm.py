from general_fsm import State, FSM


# not sure this class is necessary
class Start(State):

    def __init__(self):
        self.name = "start"
        self.inputs = ['start']
        self.outputs = ['listening']


class Listening(State):

    def __init__(self):
        self.name = "listening"
        self.inputs = ['connect', 'error']
        self.outputs = ['connected', 'error', 'listening']


class Connected(State):

    def __init__(self):
        self.name = "connected"
        self.inputs = ['accept', 'close']
        self.outputs = ['accepted', 'closed', 'error']


class Accepted(State):

    def __init__(self):
        self.name = "accepted"
        self.inputs = ['close', 'read', 'write']
        self.outputs = ['closed', 'error', 'reading', 'writing']


class Reading(State):

    def __init__(self):
        self.name = "reading"
        self.inputs = ['close', 'read', 'write']
        self.outputs = ['closed', 'error', 'reading', 'writing']


class Writing(State):

    def __init__(self):
        self.name = "writing"
        self.inputs = ['close', 'read', 'write']
        self.outputs = ['closed', 'error', 'reading', 'writing']


class Closed(State):

    def __init__(self):
        self.name = "closed"
        self.inputs = ['close']
        self.outputs = ['connected', 'error']


class Error(State):

    def __init__(self):
        self.name = "error"
        self.inputs = ['error']
        self.outputs = ['error']


if __name__ == "__main__":
    # Initialize states dict to pass to the FSM object
    states = {
        "listening": Listening(),
        "connected": Connected(),
        "accepted": Accepted(),
        "reading": Reading(),
        "writing": Writing(),
        "closed": Closed(),
        "error": Error(),
    }

    # setup the FSM object
    initial_state = states.get('listening')
    fsm = FSM(initial_state)
    fsm.states = states

    # print("The initial state is:", fsm.initial_state)
    # print("The current state is:", fsm.current_state)
    # print("The list of states is:", fsm.states)

    events = ["accept", "read", "read", "write", "close", "connect"]

    for event in events:
        fsm.next_state(event)
