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


    # def _delete(self, key, node):
    #     """Deletes the given key from the data structure."""
    #     assert node, "Invalid node given."

    #     if key < node.key:
    #         self._delete(key, node.left)
    #     elif key > node.key:
    #         self._delete(key, node.right)
    #     else:
    #         if node.left == None and node.right == None:
    #             node.parent.remove_child(node)


    def delete(self, key):
        """Delete a node from the tree if it exists."""
        # could try to write one algo to find the node, and another to delete it.
        if self.root is not None:

            node = self.root
            
            while node:
                # print("\n>>>> top while node=", node)
                if node.key == key:
                    # print(">> key==", node)
                    # the node is a leaf (no children), 
                    if node is self.root:
                        self.root = None
                        break
                    elif node.left == None and node.right == None:
                        # print(">> children=", node.left, node.right)
                        # If it's a leaf then just remove it. 
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
                            node.parent.left = node.left
                        else:
                            node.parent.right = node.right
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


    def find_min(self, node): # only in right subtrees? or call on node.right?
        # if node exists
        if node is not None:
        # start at node
            cur = node
            # go left until you reach a node without a left child
            while cur:
                if cur.left == None:
                    # return the node (or the key? or both?)
                    return cur.key
                else:
                    cur = cur.left
            # otherwise return None?
        else:
            return None


    def _invariant(self):
        # root node parent should always be None
        if self.root:
            assert self.root.parent is None, "root.parent not None"