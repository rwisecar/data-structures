"""Create a queue of tuples, (value, priority) in a priority queue."""


class Priority_Q(object):
    """
    Create a priority queue.

    insert(self, item) inserts an item into the priority queue.

    pop(self) removes the most important item from the queue.

    peek(self) returns the most important item without removing it.
    """

    def __init__(self, iterable=None):
        """Creates an instance of the Priority_Q class."""
        self._priorityq = []
        if iterable and hasattr(iterable, "__iter__"):
            for i in iterable:
                self.insert(iterable[0], iterable[1])
        elif iterable:
            raise TypeError("Can't init with a non iterable.")

    def insert(self, value, priority=0):
        """Insert value into list, if value is a tuple."""
        self._priorityq.append((value, priority))

    def pop(self):
        """Remove the most important item from the queue."""
        if not self._priorityq:
            raise IndexError("You may not pop from an empty queue.")
        top_priority = sorted(self._priorityq, key=lambda x: x[1])
        self._priorityq.remove(top_priority[0])
        return top_priority[0]

    def peek(self):
        """Return the most important item from the queue w/o removing it."""
        if not self._priorityq:
            raise IndexError("You may not pop from an empty queue.")
        top_priority = sorted(self._priorityq, key=lambda x: x[1])
        return top_priority[0]
