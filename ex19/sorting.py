from dllist import DoubleLinkedList


def bubble_sort(numbers):
    """Sorts a list of numbers using bubble sort."""
    while True:
        # start off assuming it's sorted
        is_sorted = True
        # comparing 2 at a time, skipping ahead
        node = numbers.begin.next
        while node:
            # loop through comparing node to the next
            if node.prev.value > node.value:
                # if the next is greater, then we need to swap
                node.prev.value, node.value = node.value, node.prev.value
                # oops, looks like we have to scan again
                is_sorted = False
            node = node.next

        # this is reset at the top but if we never swapped then it's sorted
        if is_sorted:
            break

# top-down merge sort using p-code from the Wikipedia page
def merge_sort(dllist: DoubleLinkedList) -> DoubleLinkedList:

    if dllist.count() == 1:
        return dllist

    left = DoubleLinkedList() # using new dllist to copy each smaller list
    right = DoubleLinkedList()

    middle = dllist.count() // 2
    lsize = middle
    rsize = dllist.count() - middle

    copy_sublist(dllist, left, lsize)
    copy_sublist(dllist, right, rsize)

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = DoubleLinkedList()
    while left.count() != 0 and right.count() != 0:
        if left.begin.value <= right.begin.value:
            result.push(left.unshift())
        else:
            result.push(right.unshift())

    while left.count() != 0:
        result.push(left.unshift())

    while right.count() != 0:
        result.push(right.unshift())
    return result


def copy_sublist(target_list: DoubleLinkedList, dest_list: DoubleLinkedList, 
                 dest_size: int) -> DoubleLinkedList:

    i = 0
    while i < dest_size:
        nodeval = target_list.unshift()
        dest_list.push(nodeval)
        i += 1

    return dest_list


def quick_sort(dllist: DoubleLinkedList, lo: int, hi: int):
    """performance:  can we replace this with a for-loop?"""
    # performance: just turn in into a python list first.
    if lo < hi:
        p = partition(dllist, lo, hi)
        quick_sort(dllist, lo, p - 1)
        quick_sort(dllist, p + 1, hi)


def partition(dllist: DoubleLinkedList, lo: int, hi: int) -> int:
    """performance:  get_node called too many times."""
    pivot = dllist.get(hi)
    index = small_index = lo

    while index < hi:
        if get_node(dllist, index).value < pivot:
            temp_i = get_node(dllist, small_index)
            temp_j = get_node(dllist, index)
            temp_i.value, temp_j.value = temp_j.value, temp_i.value
            small_index += 1
        index += 1
    # performance:  can we eliminate these? (get_node())
    temp_i = get_node(dllist, small_index)
    temp_hi = get_node(dllist, hi)
    temp_i.value, temp_hi.value = temp_hi.value, temp_i.value

    return small_index

# performance:  slowest part of quick_sort, but because it's called a lot.
def get_node(dllist: DoubleLinkedList, index: int) -> DoubleLinkedList:
    """Return the node at the given index."""
    if dllist.begin:
        count = 0
        cur = dllist.begin

        while cur:
            if index == count:
                return cur
            else:
                count += 1
                cur = cur.next
    else:
        return None

