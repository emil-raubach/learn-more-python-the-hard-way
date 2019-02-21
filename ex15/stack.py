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
        node = StackNode(obj, None)
        
        if self._top is None:
            self._top = node
            node.next = None # not needed?  Don't think so...
        else:
            node.next = self._top
            self._top = node


    def pop(self):
        """Pops the value that is currently on the top of the stack."""
        
        if self._top:
            node = self._top
            self._top = self._top.next
            node.next = None  # not needed?  Don't think so...
            return node.value
        else:
            return None

    def top(self):
        """Returns a *reference* to the first item, does not remove."""
        return self._top.value

    def count(self):
        """Counts the number of elements in the stack."""
        count = 0
        node = self._top

        while node:
            count += 1
            node = node.next

        return count

    def dump(self, mark="----"):
        """Debugging function that dumps the contents of the stack."""
    