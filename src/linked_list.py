"""Create a linked_list class with assoc. methods and instantiate."""

class LinkedList(object):

    def __init__(self, head=None, length=0):
        self.head = head
        self.length = length
        # if new_list is None:
        #     self.cargo = cargo
        #     self.next = next
        #     self.new_list = []

    def __str__(self):
        return str(self.head)

    def push(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node
        self.length = self.length + 1

    def pop(val):
        next_node = self.head.next
        node = Node(val)
        node.next = next_node
        self.head = node

        


    # def size()

    # def search(val)

    # def remove(node)

    # def display()
        # while node:
        #     print node,
        #     node = node.next
        #     print


class Node(object)
    """create linked_list from input mode"""

    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next


# # To make a new list from an old list
# new_list = [LinkedList(new_list[n]) for n in new_list]
