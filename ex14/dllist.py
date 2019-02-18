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
        # Create a new DLL node instance
        # Is the list empty?
        # If so, set start and end to the new node
        # set the new node prev and next to None
        # Increment the num nodes
        # elif the start is equal to the end (one node)
        # Set start.next to the new node
        # Set newnode.prev to start
        # set self.end = new_node
        # new_node.next is None
        # Increment the num nodes
        # otherwise (2 or more nodes?)
        # end.next = newnode
        # newnode.prev = end
        # newnode.next = None
        # end = newnode
        # increment num nodes
    
    def pop(self):
        """Removes the last item and returns it."""


    def shift(self, obj):
        """Actually just another name for push"""


    def unshift(self):
        """Removes the first item (from begin) and returns it."""


    def detach_node(self, node):
        """You'll need to use this operation sometimes, but mostly
        inside remove().  It should take a node, and detach it from 
        the list, whether the node is at the front, end, or in the middle."""


    def remove(self, obj):
        """Finds a matching item and removes it from the list."""


    def first(self):
        """Returns a *reference* to the first item, does not remove."""


    def last(self):
        """Returns a reference to the last item, does not remove."""


    def count(self):
        """Counts the number of elements in the list."""


    def get(self, index):
        """Get the value at index."""


    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""