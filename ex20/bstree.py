class BSTreeNode(object):
    
    def __init__(self, key, value, left, right, parent):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
    # This seems to lead to a recursion error when I access `.root`
    def __repr__(self):
        return (f"{self.__class__.__name__}({self.key!r}, {self.value!r}, "
                f"{self.left!r}, {self.right!r}, {self.parent!r})") 


class BSTree(object):
    
    def __init__(self):
        self.root = None
        self.num_nodes = 0


    def get(self, key):
        """Return the value of a node with the given key, or return None."""
        # are we comparing the keys or the values?  Values makes more sense...
        # start at the root
        # if self.root is not None:
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
        # else:
            # return None
        pass


    def set(self, key, value):
        """Add a new value to the tree."""
        
        if self.root is not None:

            node = self.root

            while True:    
                if key <= node.key:                    

                    if node.left:
                        node = node.left
                    else:
                        new_node = BSTreeNode(key, value, None, None, node)
                        node.left = new_node
                        self.num_nodes += 1
                        break
                elif key > node.key:
                    if node.right:
                        node = node.right
                    else:
                        new_node = BSTreeNode(key, value, None, None, node)
                        node.right = new_node
                        self.num_nodes += 1
                        break
                else:
                    break # what goes here
        else:
            self.root = BSTreeNode(key, value, None, None, None)
            self.num_nodes += 1        


    def delete(self):
        """Delete a value from the tree if it exists."""
        pass


    def list(self):
        """Print out the contents of the list."""
        pass
        # Walk the tree and print everything out. 
        # The important piece to list is that you can walk the tree in different ways to produce different output. 
        # If you walk the left, then the right paths, you get something different than if you do the inverse. 
        # If you go all the way to the bottom and then print as you come up the tree toward root, you get yet another kind of output. 
        # You can also print the nodes as you go down the tree, from root to the "leaves". 
        # Try different styles to see which one does what.
        cur = self.root

        while cur:
            pass


    def _invariant(self):
        # root node parent should always be None
        if self.root:
            assert self.root.parent is None, "root.parent not None"