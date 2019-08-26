from tstree import TSTree
from bstree import BSTree
from dllist import DoubleLinkedList


class URLNode(object):
    """Have attributes for each part of a url?  e.g., scheme, path, etc."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __repr__(self):
        return (f"{self.__class__.__name__}("
                f"{self.key!r}:{self.value!r})")


class URLRouter(object):
  
    def __init__(self):
        self.urls = []

    # TODO:  Add a method to add URLs (like `add()` or something)
    def add(self, key, value):
        self.urls.append(URLNode(key, value))

    def match_url(self, url_to_find):
        """Return an exact match of the URL."""
        rv = [path.value for path in self.urls if path.key == url_to_find]
        if rv:
            return rv[0]
        else:
            return None

    # def best_match_url(self, url_to_find):
        # """Return the best match for a URL."""
        # key = lambda x: len(x.key)
        # possible = sorted(self.url_starts_with(url_to_find), key=key)
        # return possible and possible[0] or None

    def url_starts_with(self, url_to_find):
        """Return all objects that start with `URL`."""        
        rv = [
            path.key 
            for path in self.urls
            if path.key.startswith(url_to_find)
        ]

        if rv:
            return rv
        else:
            return None


    def shortest_url(self, url_to_find):
        """Return the shortest URL matching object."""
        pass

    def longest_url(self, url_to_find):
        pass


class TSTRouter(URLRouter):

    def __init__(self):
        self.urls = TSTree()

    def add(self, key, value):
        self.urls.set(key, value)

    def match_url(self, url_to_find):
        return self.urls.get(url_to_find)

    def url_starts_with(self, url_to_find):
        return self.urls.find_all(url_to_find)

    def shortest_url(self, url_to_find):
        return self.urls.find_shortest(url_to_find)

    def longest_url(self, url_to_find):
        return self.urls.find_longest(url_to_find)


class BSTRouter(URLRouter):

    def __init__(self):
        self.urls = BSTree()

    def add(self, key, value):
        self.urls.set(key, value)

    def match_url(self, url_to_find):
        return self.urls.get(url_to_find)

    def _url_starts_with(self, results, node, url_to_find):
        if not node: return None

        if len(node.key) > len(url_to_find):
            if node.key.startswith(url_to_find):
                results.append(node.value)
        else:
            if url_to_find.startswith(node.key):
                results.append(node.value)

        if node.left:
            self._url_starts_with(results, node.left, url_to_find)
        if node.right:
            self._url_starts_with(results, node.right, url_to_find) 

    def url_starts_with(self, url_to_find):
        results = []
        self._url_starts_with(results, self.urls.root , url_to_find)
        return results


class DLLRouter(URLRouter):

    def __init__(self):
        self.urls = DoubleLinkedList()

    def add(self, key, value):
        result = self.urls.push(URLNode(key, value))
        return result

    def match_url(self, url_to_find):
        if self.urls.begin == None:  return None

        cur = self.urls.begin

        while cur:
            if cur.value.key == url_to_find:
                return cur.value.value
            else:
                cur = cur.next

        return None

    def url_starts_with(self, url_to_find):
        if self.urls.begin == None:  return None

        results = []
        cur = self.urls.begin

        while cur != self.urls.end:
            if cur.value.key.startswith(url_to_find):
                results.append(cur.value.value)
            cur = cur.next

        return results