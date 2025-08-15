class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top

        while temp is not None:
            print(temp.value)

            temp = temp.next

    class Queue:
        def __init__(self,value):
            new_node = Node(value)
            self.first = new_node
            self.last = new_node
            self.length = 1
        def print_queue(self):
            temp = self.first
            while temp is not None:
                print(temp.value)
                temp = temp.value



my_stack = Stack(4)
my_stack.print_stack()


