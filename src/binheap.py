"""An implementation of a binary heap."""


class Binheap(object):
    """
    Create a binary heap in which parent node is smallest.

    push() adds a new value into the heap.

    pop() removes the parent value from the top of the heap and returns it.

    Both push() and pop() maintain heap property.
    """

    def __init__(self, iterable=None):
        """Init method for a bin heap class."""
        self.heap = []
        if iterable is None:
            iterable = []
        for val in iterable:
            self.push(val)

    def push(self, val):
        """Push will take a value and put it in the bin heap."""
        self.heap.append(val)
        self.bubble_up(len(self.heap) - 1)

    def pop(self):
        """Pop will pop the value at the root of the heap."""
        val = self.heap[0]
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.bubble_down(0)
        self.heap = self.heap[:-1]
        return val

    def bubble_down(self, idx):
        """Bubble down until meets min heap status."""
        first_child = (2 * idx) + 1
        if first_child >= len(self.heap):
            return
        second_child = first_child + 1
        try:
            child_idx = first_child if self.heap[first_child] < self.heap[second_child] else second_child
        except IndexError:
            child_idx = first_child
        if self.heap[idx] > self.heap[child_idx]:
            self.heap[idx], self.heap[child_idx] = self.heap[child_idx], self.heap[idx]
            self.bubble_down(child_idx)

    def bubble_up(self, idx):
        """Bubble up until meets min heap status."""
        if idx == 0:
            return
        parent_idx = (idx - 1) // 2
        if self.heap[idx] < self.heap[parent_idx]:
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            self.bubble_up(parent_idx)
