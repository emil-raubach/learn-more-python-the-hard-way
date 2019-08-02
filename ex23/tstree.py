class TSTreeNode(object):

    def __init__(self, key, value, low, eq, high):
        self.key = key
        self.value = value
        self.low = low
        self.eq = eq
        self.high = high

    def __repr__(self):
        return f"{self.key}:{self.value}<{self.low and self.low.key}={self.eq and self.eq.key}={self.high and self.high.key}>"

    
class TSTree(object):

    def __init__(self):
        self.root = None

    def _get(self, node, keys):
        key = keys[0]
        if node == None:
            return None
        elif key < node.key:
            return self._get(node.low, keys)
        elif key == node.key:
            if len(keys) > 1:
                return self._get(node.eq, keys[1:])
            else:
                return node
        else:
            return self._get(node.high, keys)

    def get(self, key):
        keys = [x for x in key]    
        node = self._get(self.root, keys)
        return node and node.value or None

    def _set(self, node, keys, value):
        next_key = keys[0]
        
        if not node:
            # what happens if you add the value here?
            node = TSTreeNode(next_key, None, None, None, None)

        if next_key < node.key:
            node.low = self._set(node.low, keys, value)
        elif next_key == node.key:
            if len(keys) > 1:
                node.eq = self._set(node.eq, keys[1:], value)
            else:
                # what happens if you DO NOT add the value here?
                node.value = value
        else:
            node.high = self._set(node.high, keys, value)
        
        return node

    def set(self, key, value):
        keys = [x for x in key]
        self.root = self._set(self.root, keys, value)

    def _find_all(self, node, key, results):
        """Helper function for `find_all`"""
        # is node eq None? 
        if node.eq == None:
            # if so, add the value to the list
            results.append(node.value)

        if node.low:
            self._find_all(node.low, key, results)

        if node.eq:
            self._find_all(node.eq, key, results) 

        if node.high:
            self._find_all(node.high, key, results)


    def find_all(self, key):
        """Given a key K, find all of the key/value pairs that start with K. I would implement this first, and then base find_shortest and find_longest on that.
        """
        results = []
        keys = [x for x in key]
        start = self._get(self.root, keys)
        if start:
            self._find_all(start.eq, key, results)
        return results


    def _list(self, node, indent=0):
        """Print out the contents of the tstree."""
        assert node, "Invalid node given."

        if node:
            print(" " * indent, node.key, "=", node.value)

            if node.low:
                print(" " * indent, "<", end="")
                self._list(node.low, indent+1)
            if node.eq:
                print(" " * indent, "=", end="")
                self._list(node.eq, indent+1)
            if node.high:
                print(" " * indent, ">", end="")
                self._list(node.high, indent+1)

    def list(self, start=""):
        print("\n\n----", start)
        self._list(self.root)