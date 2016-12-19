"""Create a stack class to inherit from LinkedList class and module."""
from linked_list import LinkedList


class Stack(object):
    """Create a stack that inherits select functions from LinkedList

    push(val): adds a new node containing val to the Stack.
    pop(): removes and returns the top node from the Stack.
    size(): returns the length of the items in th Stack.
    """

    def __init__(self, head=None, data=None):
        """Create a new stack based on LinkedList composition."""
        self._linkedlist = LinkedList(head, data)

    def push(self, value):
        """Push new values to head of stack."""
        self._linkedlist.push(value)

    def pop(self):
        """Pop first value from top of stack and return."""
        try:
            return self._linkedlist.pop()
        except IndexError:
            raise IndexError("Cannot pop from an empty stack")
