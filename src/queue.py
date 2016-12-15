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
