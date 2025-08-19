class Node:
    def __init__(self,value):
        self.value = value
        self.next  = None
        self.prev  = None

class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length =1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self,value):
        new_node = Node(value)
        if self.length ==0:
            self.head  = new_node
            self.tail  = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length +=1
        return True

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def insert(self, index, value):
        if index < 0 or index > self.length:  # no insert value
            return False
        if index == 0:  # insert value without no node
            return self.prepend(value)
        if index == self.length:  # insert value at the end of node
            return self.append(value)
        # Insert in the middle of a node
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(3)

my_doubly_linked_list.insert(1,2)
my_doubly_linked_list.print_list()

