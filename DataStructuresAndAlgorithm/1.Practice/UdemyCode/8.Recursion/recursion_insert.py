
def _r_insert(self,current_node,value):
    if current_node ==None:
        return Node(value)
    if value < current_node.value:
        current_node.left = self._r_insert(current_node.left,value)
    if value > current_node.value:
        current_node.right = self._r_insert(current_node.right,value)
    return current_node

def r_insert(self,value):
    if self.root == None:
        self.root = None(value)
    self._r_insert(self.root,value)


my_tree =BinarySearchTree()
my_tree.r_insert(2)
my_tree.r_insert(3)
my_tree.r_insert(1)
