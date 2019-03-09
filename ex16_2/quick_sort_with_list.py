def quick_sort(pylist: list) -> list:
    def quick_sort_helper(pylist: list, lo: int, hi: int):
#     algorithm quicksort(A, lo, hi) is
#     if lo < hi then
        if lo < hi:
#         p := partition(A, lo, hi)
#         quicksort(A, lo, p - 1)
#         quicksort(A, p + 1, hi)

# algorithm partition(A, lo, hi) is
#     pivot := A[hi]
#     i := lo
#     for j := lo to hi - 1 do
#         if A[j] < pivot then
#             swap A[i] with A[j]
#             i := i + 1
#     swap A[i] with A[hi]
#     return i