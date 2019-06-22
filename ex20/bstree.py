class BSTreeNode(object):
    
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
    
    def __repr__(self):
        return f"{self.key}={self.value}:<--- ({self.left}) ---> ({self.right})"


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
        print(">>>>>>>>>>>>>>>>>>>>>> enter")
        if self.root is not None:

            node = self.root

            while node:   
                print(">>>> top while node=", node) 
                if node.key == key:
                    node.value = value
                    break
                elif node.left == None and node.right == None:
                    print(">> leaf==", node)
                    if key < node.key:
                        node.left = BSTreeNode(key, value, parent=node)
                        print(">> add left", node.left, "key=", key)
                    else:
                        node.right = BSTreeNode(key, value, parent=node)
                        print(">> add right", node.right, "key=", key)
                    break
                elif key < node.key:
                    print("<--- go left", node, "key=", key)
                    if node.left:
                        node = node.left
                    else:
                        node.left = BSTreeNode(key, value, parent=node)
                        print("++++ add node left", node.left, "key=", key)
                elif key >= node.key:
                    print("---> go right", node, "key=", key)
                    if node.right:
                        node = node.right
                    else:
                        node.right = BSTreeNode(key, value, parent=node)
                        print("++++ add node right", node.right, "key=", key)
                else:
                    assert False, "Should not happen."
        else:
            self.root = BSTreeNode(key, value)
            print("<<<< root=", self.root)        


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