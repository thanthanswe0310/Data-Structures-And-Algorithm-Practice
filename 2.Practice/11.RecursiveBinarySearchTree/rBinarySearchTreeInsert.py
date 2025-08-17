class Node:
    def __init__(self,value):
        self.value = value
        self.left  = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)   # ✅ create new node here
        if value == current_node.value:
            return current_node  # no duplicates
        if value < current_node.value:
            current_node.left = self._r_insert(current_node.left, value)   # ✅ assign
        else:
            current_node.right = self._r_insert(current_node.right, value) # ✅ assign
        return current_node

    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root = self._r_insert(self.root, value)

# Test
my_tree = BinarySearchTree()
my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)

print('Root:', my_tree.root.value)           # 2
print('Root -> Left:', my_tree.root.left.value)   # 1
print('Root -> Right:', my_tree.root.right.value) # 3
