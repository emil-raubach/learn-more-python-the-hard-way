import sorting
from dllist import DoubleLinkedList # can't import this...
from random import randint

max_numbers = 30

def random_list(count):
    numbers = DoubleLinkedList()
    for i in range(count, 0, -1):
        numbers.shift(randint(0, 10000))
    return numbers


def is_sorted(numbers):
    node = numbers.begin
    while node and node.next:
        if node.value > node.next.value:
            return False
        else:
            node = node.next

    return True


def test_bubble_sort():
    numbers = random_list(max_numbers)

    sorting.bubble_sort(numbers)

    assert is_sorted(numbers)


# def test_merge_sort():
#     numbers = random_list(max_numbers)

#     sorting.merge_sort(numbers)

#     assert is_sorted(numbers)