# A function that calls itself ...until it doesn't.
# 1. The process of opening each box is the same.
# 2. Each time we open a box, we make the problem smaller.
#
from Codebasis.Trees import BinarySearchTree


# open_gift_box(), Pseudo code - overview recursion

def open_gift_box():
    if 1 > 2 :
        print('Hello World!')
    open_gift_box()

# Call Stack : what is happening on the call stack

# def funcOne():
#     funcTwo()
#     print('One')
#
# def funcTwo():
#     funcThree()
#     print('Two')
#
# def funcThree():
#     print("Three")
#
# funcOne()

# Factorial : 4 * 3 * 2 * 1 = 3! - Stack structure

# def factorial(n):
#     if n ==1:
#         return 1
#     return n * factorial(n-1)
# print(factorial(4))

# Recursive Binary Trees - Contains
class BinarySearchTree:
    def _r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self._r_contains(current_node.left,value)
        if value > current_node.value:
            return self._r_contains(current_node.right,value)

    def r_contains(self,root,value):
        return True

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(34)

print('BST Contains 27: ')
print(my_tree.r_contains(7))


