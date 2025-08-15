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
    #### WRITE FIND_KTH_FROM_END FUNCTION HERE ####
    #                                             #
    #    This is a SEPARATE FUNCTION that         #
    #    is NOT a method within the               #
    #    LinkedList class.                        #
    #                                             #
    #    <== INDENT ALL THE WAY TO THE LEFT.      #
    #                                             #
    ###############################################

    first = ll.head
    second = ll.head

    for _ in range(k):
        if first is None:
            return None
        first = first.next

    while first is not None:
        first = first.next
        second = second.next
    return second


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

k = 2
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4

"""
    EXPECTED OUTPUT:
    ----------------
    4

"""

