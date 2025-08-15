class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length =1

    def print_list(self):
        temp =self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if new_node is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        return True

    def find_middle_node(self):

        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

my_linked_list = LinkedList(2)
my_linked_list.append(3)
my_linked_list.append(1)
my_linked_list.append(7)
my_linked_list.append(10)
my_linked_list.print_list()
print("Middle Node:", my_linked_list.find_middle_node().value)