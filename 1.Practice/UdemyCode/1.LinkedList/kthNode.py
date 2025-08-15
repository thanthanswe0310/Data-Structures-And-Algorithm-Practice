class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

def find_kth_from_end(ll, k):
    if ll.head is None or k <= 0:
        return None
    slow = ll.head
    fast = ll.head
    # Move fast pointer k steps ahead
    for _ in range(k):
        if fast is None:
            return None  # k is larger than the length of the list
        fast = fast.next
    # Move both pointers until fast reaches the end
    while fast:
        slow = slow.next
        fast = fast.next
    return slow


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)


k = 2
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4


