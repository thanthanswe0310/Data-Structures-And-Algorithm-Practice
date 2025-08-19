class Node:
    def __init__(self,value):
        self.value = value
        self.left  = None
        self.right = None

class BinarySearch:
    def __init__(self):
        self.root = None   # Create an empty tree

    def insert(self,value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp =self.root
        while(True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self,value):
        temp =self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False


my_tree = BinarySearch()
my_tree.insert(2)

print(my_tree.contains(1))
print(my_tree.contains(2))


# LeetCode / Interview Questions we will cover:

# Deleting a node from a BST
# Converting a sorted list to a balanced BST
# Inverting a BST
# Validating a BST








