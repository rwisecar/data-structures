"""Create a Doubly linked list."""


class Node(object):
    """Create node to push into Doubly link list."""

    def __init__(self, value=None, next_node=None, previous_node=None):
        """Create node to push into Doubly link list."""
        self.value = value
        self.next_node = next_node
        self.previous_node = previous_node


class DoubleLink(object):
    """Create a doubly linked list."""

    def __init__(self, head=None, iterable=None):
        """Create an instance of a doubly linked list."""
        self._length = 0
        self.head = None
        self.tail = None

        if iterable and hasattr(iterable, "__iter__"):
            for value in iterable:
                self.push(value)
        elif iterable:
            raise TypeError
        elif head and not iterable:
            self.push(head)

    def push(self, value):
        """Add new value to the front of a doubly linked list."""
        new_node = Node(value)
        if self.head:
            new_node.next_node = self.head
            self.head.previous_node = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self._length += 1

    def append(value):
        pass

    def pop():
        pass

    def shift():
        pass

    def remove(val):
        pass
