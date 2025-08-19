class Node:
    def __init__(self,value):
        self.value = value
        self.left = None 
        self.right = None 

class BinarySearchTree:
    def __init__(self):
        self.root = None 

my_tree = BinarySearchTree()

print(my_tree.root)


## create new_node 
# if root == None then root == new_node 
# temp = self.root 
# while loop 
#     if < left else > right 
#         if None insert new_node else move to next 

