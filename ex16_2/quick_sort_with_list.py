def quick_sort(pylist: list, lo: int, hi: int):
    if lo < hi:
        p = partition(pylist, lo, hi)
        quick_sort(pylist, lo, p - 1)
        quick_sort(pylist, p + 1, hi)


def partition(pylist, lo, hi):
    pivot = pylist[hi]
    i = j = lo
    
    while j < hi:
        if pylist[j] < pivot:
            
            pylist[i], pylist[j] = pylist[j], pylist[i]
            i += 1
        j += 1

    pylist[i], pylist[hi] = pylist[hi], pylist[i]         
    return i