class QueueNode(object):

    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f"[{self.value}, {repr(nval)}, {repr(pval)}]"


class Queue(object):

    def __init__(self):
        self._head = None
        self._tail = None
        

    def shift(self, obj):
        """Actually just another name for push"""
        node = QueueNode(obj, None, None)

        if self._head:
            if self._head.next is None:
                self._head.next = node
                node.prev = self._head
                self._tail = node
            else:
                node.prev = self._tail
                self._tail.next = node
                self._tail = node
        else:
             self._head = node
             self._tail = self._head

        
    def unshift(self):
        """Removes the first item (from begin) and returns it."""
        
        if self._head:
            node = self._head
            self._head = node.next
            if self._head:
                self._head.prev = None
            else:
                self._tail = None
            return node.value
        else:
            return None

    def front(self):
        """Returns a *reference* to the first item, does not remove."""
        return self._head.value

    def count(self):
        """Counts the number of elements in the list."""
        count = 0
        node = self._head

        while node:
            count += 1
            node = node.next

        return count


    def dump(self, mark):
        """Debugging function that dumps the contents of the queue."""
        print(">>>")
        node = self._head

        while node:
            print(repr(node))
            node = node.next

        print("<<<")

    def _invariant(self):
        if self._head is None:
            assert self._tail is None, "End tail while head is not."

        if self._head:
            assert self._head.prev is None, "head.prev not None"
            assert self._tail.next is None, "tail.next not None"