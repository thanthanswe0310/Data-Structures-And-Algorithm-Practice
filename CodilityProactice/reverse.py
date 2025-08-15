
class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None 

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node 
            self.tail = new_node
        self.length += 1
        return True
    
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def reverse(self):
        temp =self.head 
        self.head = self.tail
        self.tail = temp 

        after = temp.next
        before=None 

        for _ in range(self.length):
            after = temp.next 
            temp.next = before
            before = temp 
            temp = after 
            

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.reverse()

my_linked_list.print_list()