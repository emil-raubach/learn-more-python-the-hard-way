import merge_sort_with_list, quick_sort_with_list
from random import randint
# import pdb; pdb.set_trace()

max_numbers = 30

def random_list(count):
    numbers = list()
    for i in range(count, 0, -1):
        numbers.append(randint(0, 10000))
    return numbers


def is_sorted(numbers):
    # node = numbers.begin
    i = 0
    while i < (len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
        else:
            i += 1

    return True



# def test_merge_sort_list():
#     numbers = random_list(max_numbers)

#     merge_sort_with_list.merge_sort_list(numbers)

#     assert is_sorted(numbers)


def test_quick_sort_list():
    numbers = random_list(max_numbers*100)

    quick_sort_with_list.quick_sort(numbers, 0, (len(numbers) - 1))

    assert is_sorted(numbers)