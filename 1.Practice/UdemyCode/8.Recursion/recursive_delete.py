# Deleting a leaf node
# def _delete_node(self,current_node,value):
#     if current_node == None:
#         return None
#     if value < current_node.value:
#         current_node.left = self._delete_node(current_node.left,value)
#     elif value > current_node.value:
#         current_node.right = self._delete_node(current_node.right,value)
#     return current_node
#
#Delete Node part -2
#
#
# def _delete_node(self, current_node, value):
#     if current_node ==None:
#         return None
#     if value < current_node.value:
#         current_node.left = self._delete_node(current_node.leff, value)
#     else:
#         if current_node.left ==None and current_node.right == None:
#             return None
#         elif current_node.left == None:
#             current_node = current_node.right
#         elif current_node.right ==None:current_node = current_node.left
#         else:
#     return current_node

# Delete a Minimal value - part 3
#
# def min_value(self, current_node):
#     while current_node.left is not None:
#         current_node = current_node.left
#
#     return current_node.value
#
# print(my_tree.min_value(my_tree.root))
# print(my_tree.min_value(my_tree.root.right.value))
# print(my_tree.min_value(my_tree.root.left.value))

# Delete a node - part 4
def min_value(self,current_node):
    while(current_node.left is not None):
        current_node = current_node.left
    return current_node.value

def _delete_node(self,current_node, value):
    if current_node ==None:
        return None
    if value < current_node.value:
        current_node.left = self._delete_node(current_node.left, value)
    elif  value > current_node.value:
        current_node.right = self._delete_node(current_node.right,value)
    else:
        if current_node.left == None and current_node.right ==None:
            return None
        elif current_node.left == None:
            current_node = current_node.right
        elif current_node.right == None:
            current_node = current_node.left
        else:
            sub_tree_min = self.min_value(current_node.right)
            current_node.value = sub_tree_min
            current_node.right = self._delete_node(current_node.right, sub_tree_min)
    return current_node

def delete_node(self,value):
    self._delete_node(self.root,value)

my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(3)
my_tree.insert(5)


print("root : ",my_tree.root.value)
print("root.left = ",my_tree.root.left.value)
print("root.right= ", my_tree.root.right.value)



