# class for elements in a single linked list
class SingleLinkedListNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"


# controller class for the SLLN
class SingleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None
        self.num_nodes = 0
        

    # add a new node
    def push(self, obj):
        """Appends a new value on the end of the list."""

        if self.begin is None:
            self.begin = SingleLinkedListNode(obj, None)
            self.end = self.begin
        elif self.end is None: # don't even need this branch; begin = end!
            self.end = SingleLinkedListNode(obj, None)
            self.begin.next = self.end
        else:
            new_node = SingleLinkedListNode(obj, None)
            self.end.next = new_node
            self.end = new_node

        self.num_nodes += 1

    
    def pop(self):
        """Removes the last item and returns it."""
        
        cur = self.begin

        if cur is None:
            return None        
        elif cur.next is None:
            rv = self.begin.value
            self.begin = None
            self.num_nodes -= 1
            return rv
        else:
            while cur:  # could do:  while node.next != self.end:            
                if cur.next.next is None:
                    rv = cur.next.value
                    cur.next = None
                    self.end = cur
                    self.num_nodes -= 1
                    return rv
                else:
                    cur = cur.next


    def shift(self, obj):
        """Another name for push."""
        new_node = SingleLinkedListNode(obj, None)
        
        if self.begin is None:
            self.begin = new_node
            self.end = self.begin
            self.num_nodes += 1
        elif self.begin.next is None:
            self.end = self.begin
            self.begin = new_node
            self.begin.next = self.end
            self.num_nodes += 1
        else:
            new_node.next = self.begin
            self.begin = new_node
            self.num_nodes += 1


    def unshift(self):
        """Removes the first item and returns it."""
        
        cur = self.begin

        if cur is None:
            return None
        elif cur.next is None:  
            rv = self.begin.value          
            self.begin = None # makes self.end None too?
            self.num_nodes -= 1
            return rv
        else:
            rv = self.begin.value
            self.begin = cur.next
            self.num_nodes -= 1
            return rv

    def remove(self, obj):
        """Finds a matching item and removes it from the list."""
        
        index = 0
        cur = self.begin

        if cur is None: # no nodes; empty list
            return None
        elif cur.next is None: # only one node, self.begin
            if cur.value == obj:
                self.begin = None # use the `del` keyword?
                self.num_nodes -= 1
                return index
            else:
                return None
        else: # there are at least two nodes
            if cur.value == obj:
                self.begin = cur.next
                cur = None
                self.num_nodes -= 1
                return index # which is 0 since it's the first node
            else:
                before_cur = cur
                cur = cur.next

                while cur:
                    index += 1

                    if cur.value == obj:
                        # see if there's another node or if this is the end
                        if cur.next is None:
                            before_cur.next = None
                            cur = None
                            before_cur = self.end
                            self.num_nodes -= 1
                            return index
                        else:
                            before_cur.next = cur.next
                            cur.next = None
                            self.num_nodes -= 1
                            return index
                    else:
                        if cur.next is None:
                            return None
                        else:
                            before_cur = cur
                            cur = cur.next


    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        return self.begin.value


    def last(self):
        """Returns a reference to the last item, does not remove."""
        return self.end.value


    def count(self):
        """Return the number of elements in the list"""
        return self.num_nodes


    def get(self, index):
        """Get the value at index."""

        if self.begin is None:
            return None
        else:            
            i = 0
            cur = self.begin
            while cur:
                if index == i:
                    return cur.value
                else:
                    i += 1
                    cur = cur.next


    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""
        
        cur = self.begin
        to_print = ""

        while cur:
            if not (cur is self.end):
                to_print = to_print + str(cur.value) + ", "
            else:
                to_print = to_print + str(cur.value)

            cur = cur.next

        dump_string = f"{mark}:  {to_print}"
        print(dump_string, end=" ")