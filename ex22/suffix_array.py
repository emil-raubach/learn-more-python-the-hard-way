from bsearch_list import binary_search_list

class SuffixArraySearch(object):
    
    def __init__ (self, s_array_str):
        self.s_array_str = s_array_str

    def _parse_sarray(self, input_str):
        """Returns a sorted? list of suffixes from an input string."""
        sarray = list()

        for i in range(0, len(input_str)):
            sarray.append(input_str[i:])

        return sarray

    def find_shortest(self, beginning):
        """Return the shortest substring that has `beginning` or None."""
        sa_list = sorted(self._parse_sarray(self.s_array_str))
        # use bsearch to find the first instance of `beginning` if it exists
        index = binary_search_list(sa_list, beginning)
            # Using bsearch should work to find the smallest 
            # as its comparisons of strings shoudl be lexigraphical?
        return index, sa_list
        

    def find_longest(self, beginning):
        """Return the longest substring that has `beginning` or None."""
        # get the index of the shortest 
        shortest, sa = self.find_shortest(beginning)
        # Starting at the index of the shortest
        sa_index = [shortest]
        for i in range(shortest + 1, len(sa)):
        # check if the next suffix starts with the first letter of beginning
            if sa[i].startswith(beginning[0]): 
        # if it does, save the index to a list
                sa_index.append(i)
        # otherwise, you are done; return the last element in the index list.
        return sa_index[-1], sa

    def find_all(self, beginning):
        """Return all substrings that start with `beginning`."""
        shortest, sa = self.find_shortest(beginning)
        sa_index = [shortest]
        for i in range(shortest + 1, len(sa)):
            if sa[i].startswith(beginning[0]): 
                sa_index.append(i)
        return sa_index, sa



# Here's some idea from messing around in the interpreter
# for how to find the substrings in a suffix array
# that start with the target value.  
# magic_sa is a sorted suffix array of 'abracadabra'
# b is 'abra'

# rv = []
# for i in range(0, len(magic_sa)):
#     if magic_sa[i].startswith(b):
#         rv.append(i)