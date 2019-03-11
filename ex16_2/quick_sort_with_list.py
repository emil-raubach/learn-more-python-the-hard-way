def quick_sort(pylist: list, lo: int, hi: int):
    if lo < hi:
        print(f">>> enter if, lo is {lo} and hi is {hi}.")
        p = partition(pylist, lo, hi)
        print(">>> after partition, pylist=", pylist)
        quick_sort(pylist, lo, p - 1)
        print(f">>> after first recursive call, pylist is {pylist}, lo is {lo}, hi is {hi} and p is {p}")
        quick_sort(pylist, p + 1, hi)
        print(f">>> after second recursive call, pylist is {pylist}, lo is {lo}, hi is {hi} and p is {p}")


def partition(pylist, lo, hi):
    print("<<< enter partition, pylist=", pylist)
    pivot = pylist[hi]
    print("<<< pivot=", pivot)
    i = lo
    for j in range(lo, hi - 1):
        print(f"<<< for loop:  j={j}, lo={lo}, hi={hi}")
        if pylist[j] < pivot:
            print(f"<<< if, before swap: pylist[i]={pylist[i]}, pylist[j]={pylist[j]} and pivot={pivot}.")
            
            pylist[i], pylist[j] = pylist[j], pylist[i]
            i += 1
            print(f"<<< if, after swap: i={i}, j={j}, pylist[i]={pylist[i]}, pylist[j]={pylist[j]} and pivot={pivot}.")

    pylist[i], pylist[hi] = pylist[hi], pylist[i]         
    return i


# def swap(pylist: list, first: int, second: int):
#     temp = pylist[first]
#     pylist[first] = pylist[second]
#     pylist[second] = temp
