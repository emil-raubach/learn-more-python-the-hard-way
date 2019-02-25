# Version of bubble sort that doesn't compare the n-1th element
# procedure bubbleSort( A : list of sortable items )
def bubble_sort2(unsorted_list):
    n = unsorted_list.count()

    while True:
        is_sorted = True
        node = unsorted_list.begin.next
        i = 1   
        while i < n:
            if node.prev.value > node.value:
                node.prev.value, node.value = node.value, node.prev.value
                is_sorted = False
            node = node.next
            i += 1
        n = n - 1
        if is_sorted: break