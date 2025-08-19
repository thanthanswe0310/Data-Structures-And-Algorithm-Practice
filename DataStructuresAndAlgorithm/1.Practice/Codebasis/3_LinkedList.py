# Two main benefits over an array:
# 1. You don't need to pre-allocate space
# 2. Insertion is easier
from tables.nodes.filenode import new_node


# stock_prices => Linked list traversal = O(n)
# Accessing element by value = O(n)

class Node:
    def __init__(self,value):
        self.value = value
        self.head = None
        self.tail = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def prepend(self,value):
        new_node = Node(value)
        if self.length ==0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        return True

    def append(self,value):
        new_node = Node(value)
        if self.length ==0:
            self.head =new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        return True

    # Pop ( ) function : remove by position
    def pop(self):


    # remove ( ) function : when a value is seen in the first time, then remove that position


    def print_list(self):
        temp =self.head
        while temp:
            print(temp)
            temp = temp.next

if __name__ == "__main__":
    my_linked = LinkedList(3)
    my_linked.prepend(3)
    my_linked.append(3)
    my_linked.append(3)
    my_linked.print_list()
