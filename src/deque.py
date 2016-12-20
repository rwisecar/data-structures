"""Create a deque to inhereit from doubly linked list."""
from dll import DoubleLink


class Deque(object):
    """Create a deque and associated functions.

    append(val) adds a value to the end of the deque.

    appendleft(val) adds a value to the front of the deque.

    pop() removes a value from the end of the deque and returns it.

    popleft() removes and returns the value at the front of the deque.

    peek() returns the value after the value that would be returned by pop.

    peekleft() returns the value that would be returned by popleft.()

    size() returns the number of nodes in the deque.
    """

    def __init__(self, head=None, iterable=None):
        """Creating instances for the deque."""
        self._deque = DoubleLink(head, iterable)

    def size(self):
        """Returning the length of the deque in number of nodes."""
        if self._deque.head:
            return self._deque._length
        return 0

    def append(self, value):
        """Append the value to the end of the deque."""
        self._deque.append(value)

    def appendleft(self, value):
        """Append the value to the head of the deque."""
        self._deque.push(value)

    def pop(self):
        """Pop removes the value from the end and returns value."""
        return self._deque.shift()

    def popleft(self):
        """Popleft removes the value from the head and returns value."""
        return self._deque.pop()

    def peek(self):
        """Return value at tail."""
        if self._deque.tail is None:
            raise AttributeError("Can't peek at empty!")
        return self._deque.tail.value

    def peekleft(self):
        """Return value at head."""
        if self._deque.head is None:
            raise AttributeError("Can't peekleft at empty!")
        return self._deque.head.value
