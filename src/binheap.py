"""Create binary heap in which parent nodes are smaller than their children."""


class Binheap(object):
    """Create a binary heap in which parent node is smallest.

    push() adds a new value into the heap.

    pop() removes the parent value from the top of the heap.

    Both push() and pop() maintain heap property."""

    def __init__(self, iterable=None):
        self.heap = []
        if iterable and hasattr(iterable, "__iter__"):
            self.heap.extend(iterable)
        elif iterable:
            raise TypeError("Can't init with a non iterable.")

    # def push(self, value):
    #     """Adds a value at the end of the heap into the leftmost empty spot."""
    #     if not self.most_min:
    #         self.most_min = value
    #     elif self.most_min:
    #         while value < self[(len(self) - 1 // 2) - 1]:
    #             new_add = value
    #             old_parent = self[(len(self) - 1 // 2) - 1]
    #             new_add, old_parent = old_parent, new_add
    #     # self.current_size += 1



    # def pop(self):
        """Removes the parent element from the top of the heap and reorders."""
        # Find and remove min value
        # Take most recent node and add to head
        # Resort
        pass
