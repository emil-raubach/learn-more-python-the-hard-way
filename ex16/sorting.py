from dllist import DoubleLinkedList
from scratchpad import copy_sublist

def bubble_sort(dllist):
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
        if is_sorted: break

# top-down merge sort using p-code from the Wikipedia page
# added type hinting in the function signature
def merge_sort(dllist: DoubleLinkedList) -> DoubleLinkedList:
    # // Base case. A list of zero or one elements is sorted, by definition.
    # if length of m ≤ 1 then
    if dllist.count() <= 1:
    #     return m
        return dllist

    # // Recursive case. First, divide the list into equal-sized sublists
    # // consisting of the first half and second half of the list.
    # // This assumes lists start at index 0.
    middle = dllist.count() // 2
    lsize = middle
    rsize = dllist.count() - middle
    # var left := empty list    
    left = DoubleLinkedList()
    # var right := empty list    
    right = DoubleLinkedList()

    # create left sublist
    copy_sublist(dllist, left, lsize)
    # create right sublist
    copy_sublist(dllist, right, rsize)
    # for each x with index i in m do
    #     if i < (length of m)/2 then
    #         add x to left
    #     else
    #         add x to right

    # // Recursively sort both sublists.
    # left := merge_sort(left)
    left = merge_sort(left)
    # right := merge_sort(right)
    right = merge_sort(right)
    # // Then merge the now-sorted sublists.
    # return merge(left, right)
    return merge(left, right)


# function merge(left, right)
def merge(left, right):
#     var result := empty list
    result = list()

#     while left is not empty and right is not empty do
    while left and right:  # while both slists are not empty
        pass
        # if left list begin value <= right list begin value
#         if first(left) ≤ first(right) then
              # append (push or shift?) left begin value to result 
#             append first(left) to result
              # set left equal to remaining values in left list
#             left := rest(left)
          # else
#         else
              # append (push or shift) right begin value to result
#             append first(right) to result
              # set right equal to remaining values in right list
#             right := rest(right)

#     // Either left or right may have elements left; consume them.
#     // (Only one of the following loops will actually be entered.)
#     while left is not empty do
    # while left:    
#         append first(left) to result
          # append left begin value to result
#         left := rest(left)
          # set left equal to remaining values in left list
#     while right is not empty do
    # while right:
#         append first(right) to result
          # append (push or shift) right begin value to result
#         right := rest(right)
          # set right equal to remaining values in right list
#     return result   
#         return result 


def length(node):
    """returns the number of nodes in the dllist"""
    count = 0

    while node:
        node = node.next
        count += 1

    return count