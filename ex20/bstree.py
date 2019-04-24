class BSTreeNode(object):
    
    def __init__(self, key, value, left, right, parent):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return (f"{self.__class__.__name__}({self.key!r}, {self.value!r}, "
                f"{self.left!r}, {self.right!r}, {self.parent!r})") 


class BSTree(object):
    
    def __init__(self):
        self.root = None
        self.num_nodes = 0


    def get(self, key):
        """Return the value of a node with the given key, or return None."""
        
        # start at the root

        # if node.key = node.value (not value but key right?)
            # return node.value

        # if no left and right child:
            # return None
        # elif key < node key:
            # You go left if the given key is less-than the node's key. 
            #   node = node.left
        # else:
            # You go right if the key is greater-than the node's key. 
            # node = node.right
            
        # return None
        pass


    def set(self, key, value):
        """Add a new value to the tree."""
        
        if self.root is not None:

            node = self.root

            while True:    
                if key < node.key:                    

                    if node.left:
                        node = node.left
                    else:
                        new_node = BSTreeNode(key, value, None, None, node)
                        node.left = new_node
                        self.num_nodes += 1
                        break
                elif key >= node.key:
                    if node.right:
                        node = node.right
                    else:
                        new_node = BSTreeNode(key, value, None, None, node)
                        node.right = new_node
                        self.num_nodes += 1
                        break
                else:
                    pass # what goes here
        else:
            self.root = BSTreeNode(key, value, None, None, None)
            self.num_nodes += 1        


    def delete(self):
        """Delete a value from the tree if it exists."""
        pass


    def list(self):
        """Print out the contents of the list."""
        pass