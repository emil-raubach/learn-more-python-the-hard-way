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
    colors.get(1 == "Alizarin")
    assert colors.pop() == "Alizarin"
    assert colors.pop() == "Magenta"
    colors._invariant()


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
    colors.dump("before remove")
    assert colors.remove("Nickle Yellow") == 2
    colors.dump("after remove")
    colors._invariant()
    colors.dump("before perinone")
    assert colors.remove("Perinone") == 2
    # I added this one.
    assert colors.remove("Perinone") == None
    colors.dump("after perinone")
    assert colors.remove("Zinc White") == 1
    assert colors.remove("Cobalt") == 0


def test_first():
    colors = DoubleLinkedList()
    colors.push("Cadmium Red Light")
    assert colors.first() == "Cadmium Red Light"
    colors._invariant()
    colors.push("Hansa Yellow")
    assert colors.first() == "Cadmium Red Light"
    colors.shift("Pthalo Green")
    assert colors.first() == "Pthalo Green"
    colors._invariant()


def test_last():
    colors = DoubleLinkedList()
    colors.push("Cadmium Red Light")
    assert colors.last() == "Cadmium Red Light"
    colors.push("Hansa Yellow")
    colors._invariant()
    assert colors.last() == "Hansa Yellow"
    colors.shift("Pthalo Green")
    assert colors.last() == "Hansa Yellow"
    colors._invariant()


def test_get():
    colors = DoubleLinkedList()
    colors.push("Vermillion")
    assert colors.get(0) == "Vermillion"
    colors._invariant()
    colors.push("Sap Green")
    assert colors.get(0) == "Vermillion"
    assert colors.get(1) == "Sap Green"
    colors.push("Cadmium Yellow Light")
    assert colors.get(0) == "Vermillion"
    colors._invariant()
    assert colors.get(1) == "Sap Green"
    assert colors.get(2) == "Cadmium Yellow Light"
    assert colors.pop() == "Cadmium Yellow Light"
    assert colors.get(0) == "Vermillion"
    assert colors.get(1) == "Sap Green"
    colors._invariant()
    assert colors.get(2) == None
    colors.pop()
    assert colors.get(0) == "Vermillion"
    colors.pop()
    assert colors.get(0) == None
    colors._invariant()


