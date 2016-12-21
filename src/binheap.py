"""Create binary heap in which parent nodes are smaller than their children."""


class Binheap(object):
    """
    Create a binary heap in which parent node is smallest.

    push() adds a new value into the heap.

    pop() removes the parent value from the top of the heap.

    Both push() and pop() maintain heap property.
    """

    def __init__(self, iterable=None):
        """The init function for Binheap."""
        self.heap = []
        if iterable and hasattr(iterable, "__iter__"):
            self.heap.extend(iterable)
            self.bubble_up()
        elif iterable:
            raise TypeError("Can't init with a non iterable.")

    def push(self, value):
        """Add a value at the end of the heap into the leftmost empty spot."""
        self.heap.append(value)
        if len(self.heap) > 1:
            self.bubble_up()

    def pop(self):
        """Pop the root and return value."""
        try:
            popped_value = self.heap[0]
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            self.heap.pop()
            if len(self.heap) > 1:
                self.bubble_up()
            return popped_value
        except IndexError:
            raise IndexError("Can't pop from an empty list.")

    def bubble_up(self):
        """Sort the list."""
        child = -1
        parent = int((len(self.heap) - 2) / 2)
        while self.heap[child] < self.heap[parent]:
            self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child]
            child, parent = parent, int((parent - 1) / 2)
            if self.heap[child] is self.heap[0]:
                break
