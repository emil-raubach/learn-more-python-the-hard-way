class StackNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"


class Stack(object):

    def __init__(self):
        self._top = None

    
    def push(self, obj):
        """Pushes a new value to the top of the stack."""


    def pop(self):
        """Pops the value that is currently on the top of the stack."""


    def top(self):
        """Returns a *reference* to the first item, does not remove."""


    def count(self):
        """Counts the number of elements in the stack."""


    def dump(self, mark="----"):
        """Debugging function that dumps the contents of the stack."""
    