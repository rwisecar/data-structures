"""Create a que to inherit from Doubly link-list."""
from dll import DoubleLink


class Queue(object):
    """Create Queue to Doubly link-list."""

    def __init__(self, head=None, iterable=None):
        """Creating instances for the Queue."""
        self._queue = DoubleLink(head, iterable)

    def enqueue(self, value):
        """Adding to the back list via appending."""
        self._queue.append(value)

    def dequeue(self):
        """Remove and return the head of a queue."""
        self._queue.pop()

    def peek(self, val):
        """Search through queue for a value and return value of next node."""
        if self._queue.head:
            current = self._queue.head
            while current:
                if current.value == val:
                    if current == self._queue.tail:
                        return None
                    return current.next_node.value
                else:
                    current = current.next_node
        else:
            return None

    def size(self):
        if self._queue.head:
            return self._queue._length
        return 0
