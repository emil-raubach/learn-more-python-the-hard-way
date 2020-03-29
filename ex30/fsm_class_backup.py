# My attempt at a class-based finite state machine
# for ex30 in Learn More Python The Hard Way


class FSM(object):

    def __init__(self):
        self.state = None

    def start(self):
        return self.listening

    def listening(self, event):
        # is this how you would do it?
        self.state = "listening"

        if event == "connect":
            return self.connected
        elif event == "error":
            return self.listening
        else:
            return error

    def connected(self, event):
        self.state = "connected"

        if event == "accept":
            return self.accepted
        elif event == "close":
            return self.closed
        else:
            return self.error

    def accepted(self, event):
        self.state = "accepted"

        if event == "close":
            return self.closed
        elif event == "read":
            return self.reading(event)
        elif event == "write":
            return self.writing(event)
        else:
            return self.error

    def reading(self, event):
        self.state = "reading"

        if event == "read":
            return self.reading
        elif event == "write":
            return writing(event)
        elif event == "close":
            return self.closed
        else:
            return self.error

    def writing(self, event):
        self.state = "writing"

        if event == "read":
            return self.reading(event)
        elif event == "write":
            return self.writing
        else:
            return self.error

    def closed(self, event):
        self.state = "closed"

        return self.listening(event)

    def error():
        self.state = "error"

        return self.error
