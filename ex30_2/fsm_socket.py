from state_machine import FSM


class FSMSocket(FSM):
    start_state = 'listening'  # This seems like bad Python...

    def get_next_value(self, state, inp):
        if self.state == 'listening':
            if inp == 'connect':
                return ('connected', 'CONNECTED')
            elif inp == 'error':
                return ('listening', 'LISTENING')
            else:
                return ('error', 'ERROR')
        elif self.state == 'connected':
            if inp == 'accept':
                return ('accepted', 'ACCEPTED')
            elif inp == 'close':
                return ('closed', 'CLOSED')
            else:
                return ('error', 'ERROR')
        elif self.state == 'accepted':
            if inp == 'close':
                return ('closed', 'CLOSED')
            elif inp == 'read':
                return ('reading', 'READING')
            elif inp == 'write':
                return ('writing', "WRITING")
            else:
                return ('error', 'ERROR')
        elif self.state == 'reading':
            if inp == 'read':
                return ('reading', 'READING')
            elif inp == 'write':
                return ('writing', 'WRITING')
            elif inp == 'close':
                return ('closed', 'CLOSED')
            else:
                return ('error', 'ERROR')
        elif self.state == 'writing':
            if inp == 'read':
                return ('reading', 'READING')
            elif inp == 'writing':
                return ('writing', 'WRITING')
            elif inp == 'close':
                return ('closed', 'CLOSED')
            else:
                return ('error', 'ERROR')
        elif self.state == 'closed':
            return ('listening', 'LISTENING')
        elif self.state == 'error':
            return ('error', 'ERROR')
        else:
            pass
