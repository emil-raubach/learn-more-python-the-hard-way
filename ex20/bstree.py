class BSTreeNode(object):
    
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
    
    def __repr__(self):
        return f"{self.key}={self.value}:<---({self.left})---> ({self.right})"


class BSTree(object):
    
    def __init__(self):
        self.root = None
        self.num_nodes = 0


    def get(self, key):
        """Return the value of a node with the given key, or return None."""
        # are we comparing the keys or the values?  Values makes more sense...
        # start at the root

        if self.root is not None:
            node = self.root

            while node:
                if node.key == key:
                    return node.value
                elif node.left == None and node.right == None:
                    return None
                elif key < node.key:
                    # You go left if the given key is less-than the node's key. 
                    node = node.left
                else:
                    # You go right if the key is greater-than the node's key. 
                    node = node.right
        else:
            return None
        

    def set(self, key, value):
        """Add a new value to the tree."""
        if self.root is not None:

            node = self.root

            while node:   
                if node.key == key:
                    node.value = value
                    break
                elif node.left == None and node.right == None:
                    if key < node.key:
                        node.left = BSTreeNode(key, value, parent=node)
                    else:
                        node.right = BSTreeNode(key, value, parent=node)
                    break
                elif key < node.key:
                    if node.left:
                        node = node.left
                    else:
                        node.left = BSTreeNode(key, value, parent=node)
                elif key >= node.key:
                    if node.right:
                        node = node.right
                    else:
                        node.right = BSTreeNode(key, value, parent=node)
                else:
                    assert False, "Should not happen."
        else:
            self.root = BSTreeNode(key, value)


    def delete(self, key):
        """Delete a node from the tree if it exists."""

        if self.root is not None:

            node = self.root
            
            while node:
                if node.key == key:
                    # the node is a leaf (no children), 
                    if node.left == None and node.right == None:
                        # If it's a leaf then just remove it. 
                        if node is self.root: # special case where D is root.
                            self.root = None
                        else:
                            if node.parent.key < key:
                                node.parent.left == None
                            else:
                                node.parent.right == None
                            node.parent == None 
                        break
                    # has one child, or 
                    elif node.left or node.right:
                        # If it has one child, then replace it with the child. 
                        if node.left:
                            node = node.left
                        else:
                            node = node.right
                    # If it has two children, then it gets really complicated so read the section on deleting below.
                    elif key < node.key:
                        pass
                    else:
                        pass
                elif key < node.key:
                    node = node.left
                else:
                    node = node.right
                     
        else: # empty BSTree
            return None

    def _list(self, node):
        """Print out the contents of the list."""
        
        if node:
            self._list(node.left)
            self._list(node.right)
            print(node.key, node.value)

    def list(self):
        self._list(self.root)


    def _invariant(self):
        # root node parent should always be None
        if self.root:
            assert self.root.parent is None, "root.parent not None"