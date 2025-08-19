class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None 
        self.prev = None 

class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value) 
        self.head  = new_node
        self.tail  = new_node
        self.length = 1 

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next 
    
    def append(self,value):
        new_node =Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev  = self.tail
            self.tail = new_node
        self.length +=1
        return True
    
    def get(self, index):
        if index <0 or index >= self.length:
            return None 
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp =temp.next
        
            else: 
                temp = self.tail
                for _ in range (self.length -1,index, -1):
                    temp = temp.prev 
            return temp 
    def set_value(self, index, value):
            temp = self.get(index)
            if temp:
                temp.value = value
                return True
            return False

my_doubly_lined_list = DoublyLinkedList(11)
my_doubly_lined_list.append(3)
my_doubly_lined_list.append(23)
my_doubly_lined_list.append(7)
my_doubly_lined_list.set_value(1,4)
my_doubly_lined_list.print_list()
