"""Create binary heap in which parent nodes are smaller than their children."""


class Binheap(object):
    """Create a binary heap in which parent node is smallest.

    push() adds a new value into the heap.

    pop() removes the parent value from the top of the heap.

    Both push() and pop() maintain heap property."""

    def __init__(self, iterable=None):
        """The init function for Binheap."""
        self.heap = []
        if iterable and hasattr(iterable, "__iter__"):
            self.heap.extend(iterable)
        elif iterable:
            raise TypeError("Can't init with a non iterable.")

    # def sort_up():
    #     """Sort up."""

    def push(self, value):
        """Add a value at the end of the heap into the leftmost empty spot."""
        parent = (len(self.heap) - 1 // 2) - 1
        if len(self.heap) == 0:
            self.heap.append(value)
        else:
            self.heap.append(value)
            child = self.heap[-1]
            while child < self.heap[parent]:
                self.heap[value]
                child, parent = parent, child
                parent // 2
                

    # def pop(self):
        """Removes the parent element from the top of the heap and reorders."""
        # Find and remove min value
        # Take most recent node and add to head
        # Resort
        pass
