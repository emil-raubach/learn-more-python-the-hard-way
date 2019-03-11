def quick_sort(pylist: list, lo: int, hi: int):
    if lo < hi:
        p = partition(pylist, lo, hi)
        quick_sort(pylist, lo, p - 1)
        quick_sort(pylist, p + 1, hi)


def partition(pylist, lo, hi):
    
    swap(pylist, lo, (lo + hi) // 2)

    pivot = pylist[lo]
    small_index = lo

    for index in range(lo + 1, hi):
        if pylist[index] < pivot:
            small_index += 1
            swap(pylist, small_index, index)

    swap(pylist, lo, small_index)

    return small_index


def swap(pylist: list, first: int, second: int):
    temp = pylist[first]
    pylist[first] = pylist[second]
    pylist[second] = temp
