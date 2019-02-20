# Double Linked List Class

class DoubleLinkedListNode(object):

    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f"[{self.value}, {repr(nval)}, {repr(pval)}]"


class DoubleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None
        self.num_nodes = 0


    def push(self, obj):
        """Appends a new value on the end of the list"""

        node = DoubleLinkedListNode(obj, None, None)

        if self.begin is None:
            self.begin = node
            self.end = self.begin
            self.num_nodes += 1
        elif self.begin == self.end:
            self.begin.next = node
            node.prev = self.begin
            self.end = node
            node.next = None
            self.num_nodes += 1
        else:
            self.end.next = node
            node.prev = self.end
            node.next = None
            self.end = node
            self.num_nodes += 1
    
    def pop(self):
        """Removes the last item and returns it."""
        
        if self.end is None:
            return None
        elif self.begin == self.end:
            rv = self.end.value
            self.begin = None
            self.end = None
            self.num_nodes -= 1
            return rv
        else:
            rv = self.end.value
            self.end = self.end.prev
            self.end.next.prev is None
            self.end.next = None
            self.num_nodes -= 1
            return rv

    def shift(self, obj):
        """Actually just another name for push"""
        node = DoubleLinkedListNode(obj, None, None)
        
        if self.begin:
            if self.begin == self.end:
                self.begin = node
                node.prev = None
                node.next = self.end
                self.end.prev = node
            else:
                self.begin.prev = node
                node.next = self.begin
                self.begin = node
        else:
            self.begin = node
            self.end = self.begin

        self.num_nodes += 1

        
    def unshift(self):
        """Removes the first item (from begin) and returns it."""
        
        if self.begin:
            rv = self.begin
            if self.begin == self.end:
                self.begin = None
                self.end = None
                self.num_nodes -= 1
            else:
                self.begin = rv.next
                self.begin.prev = None
                # rv.next = None # needed?
                self.num_nodes -= 1
            return rv.value
        else:
            return None

    def detach_node(self, node):
        """You'll need to use this operation sometimes, but mostly
        inside remove().  It should take a node, and detach it from 
        the list, whether the node is at the front, end, or in the middle."""
        if node == self.begin:
            self.unshift()
        elif node == self.end:
            self.pop()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = None
            self.num_nodes -= 1

    def remove(self, obj):
        """Finds a matching item and removes it from the list."""
        if self.begin:
            index = 0
            cur = self.begin

            while cur:
                if obj == cur.value:
                    self.detach_node(cur)
                    self.num_nodes -= 1
                    return index
                else:
                    cur = cur.next
                    index += 1
        else:
            return None

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        return self.begin.value

    def last(self):
        """Returns a reference to the last item, does not remove."""
        return self.end.value

    def count(self):
        """Counts the number of elements in the list."""
        return self.num_nodes

    def get(self, index):
        """Get the value at index."""
        if self.begin:
            count = 0
            cur = self.begin

            while cur:
                if index == count:
                    return cur.value
                else:
                    count += 1
                    cur = cur.next
        else:
            return None

    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""
        cur = self.begin
        to_print = ""

        while cur:
            if not (cur is self.end):
                to_print = to_print + str(cur.value) + ", "
            else:
                to_print = '\n' + to_print + str(cur.value) + '\n'

            cur = cur.next

        dump_string = f"{mark}:  {to_print}"
        print(dump_string, end=" ")


    def _invariant(self):
        if self.begin is None:
            assert self.end is None, "End set while begin is not."

        if self.begin:
            assert self.begin.prev is None, "begin.prev not None"
            assert self.end.next is None, "end.next not None"