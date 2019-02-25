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


# def merge_sort(dllist):
    # function merge_sort(list m)
    # // Base case. A list of zero or one elements is sorted, by definition.
    # if length of m ≤ 1 then
    #     return m

    # // Recursive case. First, divide the list into equal-sized sublists
    # // consisting of the first half and second half of the list.
    # // This assumes lists start at index 0.
    # var left := empty list
    # var right := empty list
    # for each x with index i in m do
    #     if i < (length of m)/2 then
    #         add x to left
    #     else
    #         add x to right

    # // Recursively sort both sublists.
    # left := merge_sort(left)
    # right := merge_sort(right)

    # // Then merge the now-sorted sublists.
    # return merge(left, right)


# function merge(left, right)
#     var result := empty list

#     while left is not empty and right is not empty do
#         if first(left) ≤ first(right) then
#             append first(left) to result
#             left := rest(left)
#         else
#             append first(right) to result
#             right := rest(right)

#     // Either left or right may have elements left; consume them.
#     // (Only one of the following loops will actually be entered.)
#     while left is not empty do
#         append first(left) to result
#         left := rest(left)
#     while right is not empty do
#         append first(right) to result
#         right := rest(right)
#     return result    


def length(node):

    count = 0

    while node:
        node = node.next
        count += 1

    return count