class FSM(object):
    def start(self):
        self.state = self.start_state

    def step(self, inp):
        (next_state, output) = self.get_next_value(self.state, inp)
        self.state = next_state
        return output

    def transduce(self, inputs):
        self.start()
        return [self.step(inp) for inp in inputs]
