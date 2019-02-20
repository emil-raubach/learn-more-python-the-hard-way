from dllist import *
# import pdb; pdb.set_trace()

def test_push():
    colors = DoubleLinkedList()
    colors.push("Pthalo Blue")
    colors._invariant()
    assert colors.count() == 1
    colors.push("Ultramarine Blue")
    assert colors.count() == 2
    colors._invariant()
    colors.push("Magenta")
    assert colors.count() == 3


def test_pop():
    colors = DoubleLinkedList()
    colors.push("Magenta")
    colors._invariant()
    colors.push("Alizarin")
    colors.push("Tomato Red")
    assert colors.pop() == "Tomato Red"
    colors._invariant()
    assert colors.pop() == "Alizarin"
    assert colors.pop() == "Magenta"


def test_unshift():
    colors = DoubleLinkedList()
    colors.push("Viridian")
    colors.push("Sap Green")
    colors.push("Van Dyke")
    assert colors.unshift() == "Viridian"
    colors._invariant()
    assert colors.unshift() == "Sap Green"
    assert colors.unshift() == "Van Dyke"
    assert colors.unshift() == None
    colors._invariant()


def test_shift():
    colors = DoubleLinkedList()
    colors.shift("Cadmium Orange")
    assert colors.count() == 1
    colors._invariant()
    colors.shift("Carbazole Violet")
    assert colors.count() == 2
    colors.shift("Magenta")
    assert colors.count() == 3
    assert colors.pop() == "Cadmium Orange"
    colors._invariant()
    assert colors.count() == 2
    assert colors.pop() == "Carbazole Violet"
    assert colors.count() == 1
    colors._invariant()
    assert colors.pop() == "Magenta"
    assert colors.count() == 0


def test_detach_node():  # not sure about this test...
    colors = DoubleLinkedList()
    colors.push("Cadmium Orange")
    colors.push("Carbazole Violet")
    colors.push("Magenta")
    assert colors.count() == 3
    colors._invariant()
    # colors.detach_node("Carbazole Violet")
    # colors.dump("after detach")


def test_remove():
    colors = DoubleLinkedList()
    colors.push("Cobalt")
    colors.push("Zinc White")
    colors.push("Nickle Yellow")
    colors.push("Perinone")
    assert colors.remove("Cobalt") == 0
    colors.dump("before perinone")
    assert colors.remove("Perinone") == 2
    # I added this one.
    assert colors.remove("Perinone") == None
    colors.dump("after perinone")
    assert colors.remove("Nickle Yellow") == 1
    assert colors.remove("Zinc White") == 0


def test_first():
    pass


def test_last():
    pass


def test_get():
    pass



