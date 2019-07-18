from dllist import DoubleLinkedList

def binary_search_list(a_list, target):
    """Return the index of target in the sorted list, or None."""
    if not a_list:
        return None
    else:
        begin = 0
        end = len(a_list) - 1
        mid = (end + begin) // 2 
        while begin <= end:
            mid = (end + begin) // 2 
            if target == a_list[mid]:
                return mid
            else:
                if target < a_list[mid]:
                    end = mid - 1
                else:
                    begin = mid + 1


def binary_search_dllist(dllist, target):
    # if the dllist is empty, return None
    if dllist.count() == 0:
        return None
    # otherwise
    else:
        begin = 0
        end = dllist.count() - 1
        while begin <= end:
            mid = (end + begin) // 2
            if target == dllist.get(mid):
                return mid
            else:
                if target < dllist.get(mid):
                    end = mid - 1
                else:
                    begin = mid + 1


def bsearch_list_alt(a_list, target):
    # Set L to 0 and R to n - 1
    # If L = R, go to step 6.
    # Set m to the ceiling of (L + R) / 2, 
    # which is the least integer greater than or
    # equal to (L + R) / 2.
    # If A_m > T, set R to m - 1 and go to step 2.
    # Set L to m and go to step 2.
    # Now L = R, the search is done.  If A_L = T, return L.
    # Otherwise, the search terminates as unsuccessful.