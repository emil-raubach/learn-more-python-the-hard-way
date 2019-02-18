from dllist import *
# import pdb; pdb.set_trace()

def test_push():
    colors = DoubleLinkedList()
    colors.push("Pthalo Blue")
    assert colors.count() == 1
    colors.push("Ultramarine Blue")
    assert colors.count() == 2
