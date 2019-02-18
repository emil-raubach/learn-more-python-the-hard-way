from dllist import *
# import pdb; pdb.set_trace()

def test_push():
    colors = DoubleLinkedList()
    colors.push("Magenta")
    colors.count() == 1
