# sandbox for messing around with some simple alogrithms
# that I am trying to use with merge sort

from dllist import DoubleLinkedList
from sorting import length
from random import randint

# need to break a dllist into two sublists
# one idea is to create copies using the dllist
# unshift and push methods.
number = randint(5, 10)

start_list = DoubleLinkedList()
left = DoubleLinkedList()
right = DoubleLinkedList()

for i in range(number):
    start_list.push(randint(0, 10))

start_list.dump("start list initialized.")

lsize = start_list.count()
print("\nlsize is: ", lsize)
mid = lsize // 2
print("\nmid is: ", mid)

left_size = mid
right_size = lsize - mid
print(f"\nThe length of left is {left_size} & right is {right_size}.")

# copy half of the list into left
i = 0
while i < mid:
    nodeval = start_list.unshift()
    left.push(nodeval)
    i += 1

start_list.dump("start after left copy")
left.dump("left after copying from start")

j = 0
while j < right_size:
    # print(">>> start of while:  j is", j, " and right_size is", right_size)
    nodeval = start_list.unshift()
    # print(">>> nodeval is ", nodeval)
    right.push(nodeval)
    # right.dump(f"right at {j} is ")
    j += 1

print()
start_list.dump("start after right copy")
print()
right.dump("right after copying from start")
print()