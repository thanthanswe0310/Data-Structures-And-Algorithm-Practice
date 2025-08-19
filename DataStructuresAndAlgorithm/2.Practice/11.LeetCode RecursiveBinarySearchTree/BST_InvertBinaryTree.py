class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.__r_insert(self.root, value)

    def invert(self):
        self.root = self.__invert_tree(self.root)

    # Private method to invert the tree
    def __invert_tree(self, node):
        if node is None:
            return None
        # Swap left and right children
        node.left, node.right = node.right, node.left
        # Recursively invert left and right subtrees
        self.__invert_tree(node.left)
        self.__invert_tree(node.right)
        return node
