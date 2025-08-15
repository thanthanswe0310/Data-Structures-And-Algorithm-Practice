class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node 
        self.tail = new_node
        self.length=1

    def append(self,value):
        new_node = Node(value)
        if self.length ==0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail      = new_node 
        self.length +=1 
        return True 
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next


    def insert(self,index,value):
        if index <0 or index > self.length:
            return False
        if index ==0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node 
        self.length += 1
        return True


my_linked_list = LinkedList(0)
my_linked_list.append(2)

my_linked_list.print_list()

    

