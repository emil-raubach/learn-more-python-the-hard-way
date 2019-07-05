def binary_search_list(a_list, target):
    """Return the index of target in the sorted list, or None."""
    if not a_list:
        print("\n>>>> empty list", a_list)
        return None
    else:
        begin = 0
        end = len(a_list) - 1
        mid = (end + begin) // 2 
        while begin <= end:
            mid = (end + begin) // 2 
            print("\n\n>>>> start while, target=", target, "begin=", begin, 
                  "end=", end, "mid=", mid, "a_list=", a_list)
            if target == a_list[mid]:
                print("<<< match: target=", target, "a_list[mid]=", a_list[mid])
                return mid
            else:
                if target < a_list[mid]:
                    end = mid - 1
                    print("\n>>> target < a_list[mid], target=", target, "begin=", begin, "end=", end, "mid=", mid, "a_list=", a_list)
                else:
                    begin = mid + 1
                    print("\n>>> target > a_list[mid], target=", target, "begin=", begin, "end=", end, "mid=", mid, "a_list=", a_list)