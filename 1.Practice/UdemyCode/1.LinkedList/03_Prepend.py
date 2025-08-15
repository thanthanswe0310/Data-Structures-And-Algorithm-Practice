class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
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


    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node 
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    




    def print_list(self):
        temp =self.head
        while temp:
            print(temp)
            temp = temp.next

        
if __name__ =="__main__":
    my_linked_list = LinkedList(2)
    my_linked_list.append(3)
    my_linked_list.prepend(1)
    my_linked_list.print_list()
