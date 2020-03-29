# My attempt at a class-based finite state machine
# for ex30 in Learn More Python The Hard Way


class FSM(object):

    def __init__(self):
        self.state = None

    def start(self):
        self.state = "start"
        self.print_current_state()

    def connect(self):
        if self.state == "start":
            self.state = 'listening'
        elif self.state == 'error':
            self.state = 'listening'
        else:
            self.state = 'error'

    def accept(self):
        pass

    def close(self):
        pass

    def read(self):
        pass

    def write(self):
        pass

    def error(self):
        pass

    def print_current_state(self):
        if self.state is None:
            print(f'The current state is {self.state}.')
        else:
            print(f'The state has changed to {self.state}.')
        