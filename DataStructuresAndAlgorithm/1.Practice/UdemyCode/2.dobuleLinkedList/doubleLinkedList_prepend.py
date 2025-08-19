class Node:
    def __init__(self,value):
        self.value = value
        self.head = None
        self.tail = None 

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
            
    def prepend(self,value):
        new_node = Node(value)
        if self.length ==0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length +=1
        return True
    
my_doubly_linked_list = DoubleLinkedList(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.print_list()