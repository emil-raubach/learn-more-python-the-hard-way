from bsearch import binary_search_list, binary_search_dllist
from dllist import DoubleLinkedList
from random import randint
from sorting import merge_sort


def random_list(count):
    numbers = []
    for i in range(count, 0, -1):
        numbers.append(randint(0, 10000))
    return list(set(numbers))


def random_dllist(count):
    numbers = DoubleLinkedList()
    for i in range(count, 0, -1):
        numbers.shift(randint(0, 10000))
    return numbers


def test_bsearch():
    bslist = []
    # test case 1: empty list
    assert binary_search_list(bslist, 'test') == None
    bslist.append(1)
    # test case 2: list with one element
    assert binary_search_list(bslist, 1) == 0
    # test case 3: list with two elements
    bslist.append(4)
    assert binary_search_list(bslist, 4) == 1
    # test case 4: list with more than two elements
    bslist.append(7)
    bslist.append(12)
    bslist.append(19)
    assert binary_search_list(bslist, 35) == None
    assert binary_search_list(bslist, 12) == 3
    # test case 5: list with an even number of elements
    bslist.append(35)
    assert binary_search_list(bslist, 2) == None
    assert binary_search_list(bslist, 1) == 0
    assert binary_search_list(bslist, 35) == 5
    # test an unsorted list
    unsort = [4, 19, 35, 1, 7, 9]
    binary_search_list(unsort, 5)


def test_bsearch_dllist():
    numbers = DoubleLinkedList()
    assert binary_search_dllist(numbers, 1) == None
    numbers.push(1)
    assert binary_search_dllist(numbers, 1) == 0
    numbers.push(4)
    assert binary_search_dllist(numbers, 4) == 1
    numbers.push(7)
    numbers.push(9)
    numbers.push(12)
    numbers.push(19)
    assert binary_search_dllist(numbers, 35) == None
    assert binary_search_dllist(numbers, 12) == 4
    numbers.push(35)
    assert binary_search_dllist(numbers, 2) == None
    assert binary_search_dllist(numbers, 1) == 0
    assert binary_search_dllist(numbers, 35) == 6


def test_performance():

    data = sorted(random_list(1000))
    for i, v in enumerate(data):
        index = binary_search_list(data, data[i])
        assert index == i

    data = merge_sort(random_dllist(1000)) # can't get this to work right now...
    for i in range(data.count()):
        print(">>>> i=", i)
        index = binary_search_dllist(data, data.get(i))
        print(">>> index=", index, 'data.get(i)=', data.get(i))
        assert index == i

def do_performance(sort_func, count):
    data = sorted(random_list(count))
    for i, v in enumerate(data):
        index = sort_func(data, data[i])
        assert index == i

def test_do_performance():
    do_performance(binary_search_list, 1000)
    do_performance(binary_search_dllist, 1000)
    # example has one for btree, recursive and iterative one's for list


# if __name__ == "__main__":
#     for i in range(100000):
#         test_bsearch()
#         test_bsearch_dllist()