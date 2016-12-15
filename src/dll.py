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

    def append(self, value):
        """Add a new value to the end of a doubly linked list."""
        new_node = Node(value)
        if self.tail:
            self.tail.next_node = new_node
            new_node.previous_node = self.tail
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self._length += 1

    def pop(self):
        """Remove and return head of a dll."""
        if self.head is None:
            raise IndexError("Cannot pop from an empty list.")
        next_node = self.head.next_node
        old_head = self.head
        self.head = next_node
        self.head.previous_node = None
        self._length = self._length - 1
        return old_head.value

    def shift(self):
        """Remove and return the tail of a dll."""
        if self.tail is None:
            raise IndexError("Cannot shift from an empty list.")
        prev_node = self.tail.previous_node
        old_tail = self.tail
        self.tail = prev_node
        self._length = self._length - 1
        return old_tail.value

    def remove(self, val):
        """Input a value and remove a node with that value from the list."""
        current = self.head
        previous = current.previous_node
        following = current.next_node
        found = False
        while current and found is False:
            if current.value == val:
                if previous is None:
                    self.pop()
                else:
                    previous.next_node = following
                    following.previous_node = previous
                self._length -= 1
                found = True
            previous = current
            current = previous.next_node
            following = current.next_node
