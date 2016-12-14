"""Create a stack class to inherit from LinkedList class and module."""
from linked_list import LinkedList, Node


class Stack(object):
    """Create a stack that inherits select functions from LinkedList"""

    def __init__(self, head=None, data=None, length=0):
        """Create a new stack based on LinkedList composition."""
        self._linkedlist = LinkedList()
        if data:
            try:
                for item in data:
                    self._linkedlist.head = Node(item)
                    self._linkedlist.length = 1
            except TypeError:
                self._linkedlist.head = data
        else:
            self._linkedlist.head = head
            self._linkedlist.length = length

    def push(self, value):
        self._linkedlist.push(value)

    def pop(self):
        self._linkedlist.pop()

    def size(self):
        self._linkedlist.size()


# new_stack = Stack(data=[1])
# print(new_stack._linkedlist.head.value)
# new_stack._linkedlist.pop()
# print(new_stack._linkedlist.head.value)
