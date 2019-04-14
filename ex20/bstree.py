class BSTreeNode(object):
    
    def __init__(self, key, value, left, right, parent):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


class BSTree(object):
    
    def __init__(self):
        pass


    def get(self, key):
        """Return the value of a node with the given key, or return None."""
        # Given a key, walk the tree to find the node, or return None if you reach a dead end. 

        # start at the root
        # You go left if the given key is less-than the node's key. 
        if key < node key:
            # go left
        else:
            # You go right if the key is greater-than the node's key. 
            # go right
            
        # If you read a node with no left or right, then you're done and the node does not exist. 
        # There is a way to do this using recursion and using a while loop.


    def set(self, key, value):
        """Add a new value to the tree."""
        pass


    def delete(self):
        """Delete a value from the tree if it exists."""
        pass


    def list(self):
        """Print out the contents of the list."""
        pass


    def list(self):
        pass