from stack import *
# import pdb; pdb.set_trace()

def test_push():
    colors = Stack()
    colors.push("Magenta")
    assert colors.count() == 1
    colors.push("Orange")
    colors.push("Pthalo Blue")
    assert colors.count() == 3


def test_pop():
    colors = Stack()
    colors.push("Pthalo Blue")
    colors.push("Tomato Red")
    colors.push("Violet")
    assert colors.count() == 3
    assert colors.pop() == "Violet"
    assert colors.count() == 2
    assert colors.pop() == "Tomato Red"
    assert colors.pop() == "Pthalo Blue"
    assert colors.pop() == None
    assert colors.count() == 0


def test_top():
    colors = Stack()
    colors.push("Magenta")
    assert colors.top() == "Magenta"
    colors.push("Fandango")
    assert colors.top() == "Fandango"
    colors.pop()
    assert colors.top() == "Magenta"
    

