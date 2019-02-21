from queue import *
# import pdb; pdb.set_trace()

def test_shift():
    colors = Queue()
    colors.shift("Fandango")
    assert colors.count() == 1
    colors._invariant()
    colors.shift("Violet")
    assert colors.count() == 2
    colors.shift("Pthalo Blue")
    assert colors.count() == 3
    colors._invariant()
    colors.shift("Tomato Red")
    assert colors.count() == 4
    assert colors.front() == "Fandango"


def test_unshift():
    colors = Queue()
    colors.shift("Magenta")
    colors.shift("Pthalo Blue")
    colors.shift("Orange")
    assert colors.unshift() == "Magenta"
    colors._invariant()
    assert colors.unshift() == "Pthalo Blue"
    assert colors.unshift() == "Orange"
    assert colors.unshift() == None
    colors._invariant()

