from tstree import TSTree

# I think I need a URL class that will contain the actual URLs.
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

    # TODO:  Add a method to add URLs (like `new_url()` or something)
    def new_url(self, key, value):
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

    def new_url(self, key, value):
        self.urls.set(key, value)

    def match_url(self, url_to_find):
        return self.urls.get(url_to_find)

    def url_starts_with(self, url_to_find):
        return self.urls.find_all(url_to_find)

    def shortest_url(self, url_to_find):
        return self.urls.find_shortest(url_to_find)

    def longest_url(self, url_to_find):
        return self.urls.find_longest(url_to_find)