def quick_sort(pylist: list, lo: int, hi: int):
    if lo < hi:
        p = partition(pylist, lo, hi)
        quick_sort(pylist, lo, p - 1)
        quick_sort(pylist, p + 1, hi)


def partition(pylist, lo, hi):
    print(">>> enter partition lo", lo, "hi", hi)
    pivot = pylist[hi]
    small_index = index = lo

    while index < hi:
        if pylist[index] < pivot:
            print(">>>> LESS before swap small_index", small_index, "index", index, "pylist[small_index]", pylist[small_index], "pylist[index]", pylist[index])
            pylist[small_index], pylist[index] = pylist[index], pylist[small_index]
            print(">>>> LESS after swap small_index", small_index, "index", index, "pylist[small_index]", pylist[small_index], "pylist[index]", pylist[index])
            small_index += 1
        index += 1
    pylist[small_index], pylist[hi] = pylist[hi], pylist[small_index]         
    return small_index