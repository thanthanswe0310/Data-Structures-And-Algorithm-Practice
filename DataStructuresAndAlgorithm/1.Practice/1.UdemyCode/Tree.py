class Node:
    def __init__(self,value):
        self.value = value
        self.left = Node
        self.right = Node


class BinarySearch()
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while(temp):
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp.left = new_node
            elif new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp.right = new_node
    def contains(self,value):
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right

            else:
                return True
            return False


my_tree = BinarySearch()

my_tree.insert(3)
my_tree.insert(13)
my_tree.insert(43)

print(my_tree.contains(9))
print(my_tree.contains(12))



