# Basically going to try to copy the MIT OCW 6.01 SM class
class FSM(object):
    def start(self):
        self.start = self.start_state

    def step(self, inp):
        (next_state, output) = self.get_next_value(self.state, inp)
        self.state = next_state
        return output

    def transduce(self, inputs):
        self.start()
        return [self.step(inp) for inp in inputs]