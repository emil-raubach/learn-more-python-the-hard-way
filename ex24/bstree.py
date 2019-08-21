class BSTreeNode(object):
    
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
    
    def find_minimum(self):
        node = self
        while node.left:
            node = node.left
        return node

    def replace_child(self, child):
        """Given a child, it will find the child, move it's value to here,
        then remove it.  Copied from wikipedia to solve it quicker.
        """
        if self.parent:
            if self == self.parent.left:
                self.parent.left = child
            else:
                self.parent.right = child

        if child:
            child.parent = self.parent

    def __repr__(self):
        return f"{self.key}={self.value}:<---({self.left})---> ({self.right})"


class BSTree(object):
    
    def __init__(self):
        self.root = None
        self.num_nodes = 0

    # iterative 'find' function
    def get(self, key):
        """Return the value of a node with the given key, or return None."""
        
        if self.root is not None: # could use `if not self.root` ala Zed
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
                if node.key == key: # this handles duplicates?
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


    def _delete(self, key, node):
        """Deletes the given key from the data structure."""
        assert node, "Invalid node given."

        if key < node.key:
            self._delete(key, node.left)
        elif key > node.key:
            self._delete(key, node.right)
        else:
            if node.left and node.right:
                successor = node.find_minimum()
                node.key = successor.key
                self._delete(successor.key, successor)
            elif node.right:
                if self.root == node:
                    self.root = node.right
                else:
                    node.replace_child(node.right)
            elif node.left:
                if self.root == node:
                    self.root = node.left
                else:
                    node.replace_child(node.left)
            else:
                if self.root == node:
                    self.root = None
                else:
                    node.replace_child(None)


    def delete(self, key):
        """Delete a node from the tree if it exists."""
        if self.root:
            self._delete(key, self.root)


    def _list(self, node, indent=0):
        """Print out the contents of the list."""
        assert node, "Invalid node given."

        if node:
            print(" " * indent, node.key, "=", node.value)
            
            if node.left:
                print(" " * indent, "<", end="")
                self._list(node.left, indent+1)
            if node.right:
                print(" " * indent, ">", end="")
                self._list(node.right, indent+1)


    def list(self, start=""):
        print("\n\n----", start)
        self._list(self.root)


    def _invariant(self):
        # root node parent should always be None
        if self.root:
            assert self.root.parent is None, "root.parent not None"