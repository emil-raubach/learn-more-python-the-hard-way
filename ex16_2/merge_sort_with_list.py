# Try to implement merge sort from the p-code on Wikipedia using Python's 
# built-in lists before trying to do it using my own DoubleLinkedList
def merge_sort_list(pylist: list) -> list:
    if len(pylist) <= 1:
        print(">>> base case: ", pylist)
        return pylist

    left = []
    right = []

    for i, elem in enumerate(pylist):
        if i < len(pylist) // 2:
            left.append(elem)
        else:
            right.append(elem)
    print(">>> left is=", left)
    print(">>> right is=", right)
    left = merge_sort_list(left)
    right = merge_sort_list(right)

    return merge(left, right)


def merge(left: list, right: list):
    result = []
    print("<<< entering merge...")
    print(f"<<< before while, left is {left}, and right is {right}.")
    while left and right:

        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    print(f"<<< after 1st while left is {left}, and right is {right}.")
    print("<<< result=", result)
    while left:
        result.append(left.pop(0))

    while right:
        result.append(right.pop(0))

    return result