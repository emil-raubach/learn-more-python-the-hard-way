from dllist import DoubleLinkedList
from scratchpad import copy_sublist


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
# added type hinting in the function signature
# As of 27Feb2019 this is not working at all...
def merge_sort(dllist: DoubleLinkedList) -> DoubleLinkedList:

    # if dllist.count() == 1:
    if dllist.next == None:
        print(">>> base case: dllist=", dllist.dump("base case"))
        return dllist

    left = DoubleLinkedList() # using new dllist to copy each smaller list
    right = DoubleLinkedList()

    middle = dllist.count() // 2
    print(">>> middle=", middle)
    lsize = middle
    print(">>> lsize=", lsize)
    rsize = dllist.count() - middle
    print(">>> rsize=", rsize)

    copy_sublist(dllist, left, lsize)
    copy_sublist(dllist, right, rsize)

    left = merge_sort(left)
    print(">>> ", left.dump("left="))
    right = merge_sort(right)
    print(">>> will this even run? right=", right.dump("right="))
    return merge(left, right)


def merge(left, right):
    result = DoubleLinkedList()
    print("<<< entering merge...")
    print(f"<<< before while, left is {left.begin}, and right is {right.begin}.")
    while left is not None and right is not None:  # while both slists are not empty
        print(f"<<< enter while - left=", left.begin, "right=", right.begin)
        if left.begin.value <= right.begin.value:
            print("<<< if-branch: left=", left.begin, "right=", right.begin)
            result.push(left.unshift())
            print("<<< result=", result.dump("result"))
        else:
            print("<<< else-branch:  left=", left.begin, "right=", right.begin)
            result.shift(right.unshift())
            print("<<< result=", result.dump("result"))

    print(f"<<< after 1st while - left is {left.begin}, and right is {right.begin}.")
    print("<<< result=", result)
    while left:
        result.shift(left.unshift())

    while right:
        result.shift(right.unshift())

    return result


def length(node):
    """returns the number of nodes in the dllist"""
    count = 0

    while node:
        node = node.next
        count += 1

    return count


def quick_sort():
    pass