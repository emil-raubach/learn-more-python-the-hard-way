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
                # head.next = node
                self._head.next = node
                # node.prev = head
                node.prev = self._head
                # point tail at new node
                self._tail = node
            else:
                # new node.prev = tail
                node.prev = self._tail
                # tail.next = node
                self._tail.next = node
                # set tail to new node
                self._tail = node
        else:
             self._head = node
             self._tail = self._head

        
    def unshift(self):
        """Removes the first item (from begin) and returns it."""
        # if not empty
            # save head
            # node = head
            # head = node.next
            # if head
                # head.prev = None
            # else
                # tail = None
        # else
            # return None

    def front(self):
        """Returns a *reference* to the first item, does not remove."""
                

    def count(self):
        """Counts the number of elements in the list."""
        count = 0
        node = self._head

        while node:
            count += 1
            node = node.next

        return count


    def _invariant(self):
        if self._head is None:
            assert self._tail is None, "End tail while head is not."

        if self._head:
            assert self._head.prev is None, "head.prev not None"
            assert self._tail.next is None, "tail.next not None"