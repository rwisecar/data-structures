"""Create a stack class to inherit from LinkedList class and module."""
from linked_list import LinkedList, Node


class Stack(object):
    """Create a stack that inherits select functions from LinkedList"""

    def __init__(self, head=None, data=None, length=0):
        """Create a new stack based on LinkedList composition."""
        self._linkedlist = LinkedList(head, data, length)

    def push(self, value):
        """Push new values to head of stack."""
        self._linkedlist.push(value)

    def pop(self):
        """Pop first value from top of stack and return."""
        try:
            return self._linkedlist.pop()
        except IndexError:
            raise IndexError("Cannot pop from an empty stack")

    def size(self):
        self._linkedlist.size()
