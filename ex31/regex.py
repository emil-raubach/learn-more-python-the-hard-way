from state_machine import FSM


# regex class for the expression `^[A-Z]+`
class RegEx(FSM):
    def __init__(self):
        self.start_state = 0

    def get_next_value(self, state, inp):
        """Override parent class method to add
        specific logic for getting the next
        state and output.
        """
        if self.state == 0 and inp >= 'A' and inp <= 'Z':
            return (1, 'ACCEPT')
        elif self.state == 1 and inp >= 'A' and inp <= 'Z':
            return (1, 'ACCEPT')
        else:
            return (3, 'REJECT')
