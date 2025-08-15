
def dfs_in_order(self):
    results =[]
    def traverse(current_node):
        if current_node.left is not None:
            traverse(current_node.left)
        results.append(current_node.value)
        if current_node.right is not None:
            traverse(current_node.right)

    traverse(self.root)
    return results

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(17)
my_tree.insert(27)
my_tree.insert(41)
my_tree.insert(11)
