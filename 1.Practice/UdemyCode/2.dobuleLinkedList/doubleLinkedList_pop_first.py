class Node:
    def __init__(self,value):
        self.value = value 
        self.next  = None 
        self.prev  = None 

class DoubleLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head= new_node
        self.tail= new_node
        self.length = 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next 

    def pop_first(self):
        if self.length ==0:
            return None 
        temp = self.head 
        if self.length ==1:
            self.head = None 
            self.tail = None 
        else:
            self.head = self.head.next
            self.head.prev = None 
            temp.next = None 
        self.length -= 1
        return temp.value

my_dobuly_linked_list = DoubleLinkedList(2)
my_dobuly_linked_list.append(1)

# (2) Items - Returns 2 Node
print(my_dobuly_linked_list.pop_first())
# (1) Items - Returns 1 Node
print(my_dobuly_linked_list.pop_first())
# (0) Items - Returns None
print(my_dobuly_linked_list.pop_first())