from queue import *
# import pdb; pdb.set_trace()

def test_shift():
    colors = Queue()
    colors.shift("Fandango")
    assert colors.count() == 1
    colors._invariant()
    colors.shift("Violet")
    assert colors.count() == 2
    # colors.shift("Pthalo Blue")
    # assert colors.count() == 3

