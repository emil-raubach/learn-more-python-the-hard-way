from state_machine import FSM


class FSMSocket(FSM):
    start_state = 'listening'

    def get_next_values(self, state, inp):
        return 'what?'