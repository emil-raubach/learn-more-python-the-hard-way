from bsearch import binary_search_list

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
    print(bslist)
    assert binary_search_list(bslist, 12) == 3

    # test case 5: list with an even number of elements
    bslist.append(35)
    assert binary_search_list(bslist, 2) == None
    assert binary_search_list(bslist, 1) == 0
    assert binary_search_list(bslist, 35) == 5