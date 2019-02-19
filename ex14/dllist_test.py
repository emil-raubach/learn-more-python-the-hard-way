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