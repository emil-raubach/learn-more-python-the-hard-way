from bstree import BSTree

def test_BSTree_set():
    numbers = BSTree()
    numbers.set('one', 1)
    assert numbers.root.value == 1
    numbers.set('one', 'uno')
    numbers._invariant()
    assert numbers.root.key == 'one'
    assert numbers.root.value == 'uno'
    numbers.set('three', 3)
    assert numbers.root.right.key == 'three'
    numbers.set('four', 4)
    numbers._invariant()
    assert numbers.root.left.key == 'four'
    return numbers

def test_BSTree_get():
    numbers = test_BSTree_set()
    assert numbers.get('one') == 'uno'
    numbers._invariant()
    assert numbers.get('three') == 3
    numbers.set('six', 6)
    assert numbers.get('six') == 6


def test_BSTree_list():
    numbers = test_BSTree_set()
    numbers.list()


def test_delete():
    numbers = test_BSTree_set()
    numbers.delete('one')
    assert numbers.get('one') == None