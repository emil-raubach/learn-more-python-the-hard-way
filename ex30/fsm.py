from fsm_class import FSM


class FSMSocket(FSM):

    def START(self):
        return self.LISTENING

    def LISTENING(self, event):
        if event == "connect":
            return self.CONNECTED
        elif event == "error":
            return self.LISTENING
        else:
            return self.ERROR

    def CONNECTED(self, event):
        if event == "accept":
            return self.ACCEPTED
        elif event == "close":
            return self.CLOSED
        else:
            return self.ERROR

    def ACCEPTED(self, event):
        if event == "close":
            return self.CLOSED
        elif event == "read":
            return self.READING(event)
        elif event == "write":
            return self.WRITING(event)
        else:
            return self.ERROR

    def READING(self, event):
        if event == "read":
            return self.READING
        elif event == "write":
            return self.WRITING(event)
        elif event == "close":
            return self.CLOSED
        else:
            return self.ERROR

    def WRITING(self, event):
        if event == "read":
            return self.READING(event)
        elif event == "write":
            return self.WRITING
        elif event == "close":
            return self.CLOSED
        else:
            return self.ERROR

    def CLOSED(self, event):
        return self.LISTENING(event)

    def ERROR(self, event):
        return self.ERROR