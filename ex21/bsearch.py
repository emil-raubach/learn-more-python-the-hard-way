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