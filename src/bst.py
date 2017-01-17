"""An implementation of a binary search tree."""


class Node(object):
    """Create node to for use in a binary search tree."""

    def __init__(self, value=None, left_child=None, right_child=None):
        """Create node to push into Doubly link list."""
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


class BST(object):
    """The Binary search tree class."""

    def __init__(self, iterable=None):
        """Initialize a binary search tree."""
        self.root = None
        self._size = 0
        if iterable and hasattr(iterable, "__iter__"):
            for i in iterable:
                self.insert(i)
        elif iterable:
            raise TypeError("Can't init with a non iterable.")

    def insert(self, value):
        """Insert value into the binary search tree."""
        if self.root:
            self._insert(value, self.root)
        else:
            self.root = Node(value)
            self._size += 1

    def _insert(self, value, node):
        if value == node.value:
            pass
        elif value > node.value:
            if node.right_child:
                self._insert(value, node.right_child)
            else:
                node.right_child = Node(value)
                self._size += 1
        else:
            if node.left_child:
                self._insert(value, node.left_child)
            else:
                node.left_child = Node(value)
                self._size += 1

    def search(self, value):
        """Return the node containing val."""
        return self._search(value, self.root)

    def _search(self, value, node):
        if node.value == value:
            return node
        elif value > node.value:
            if node.right_child:
                return self._search(value, node.right_child)
            else:
                return None
        else:
            if node.left_child:
                return self._search(value, node.left_child)
            else:
                return None

    def size(self):
        """Return the size of the binary search tree."""
        return self._size

    def depth(self):
        """Return the depth of the binary search tree."""
        return self._depth(self.root)

    def _depth(self, node):
        """Helper for depth method."""
        if node is None:
            return 0
        else:
            return max(self._depth(node.left_child), self._depth(node.right_child)) + 1

    def contains(self, value):
        """Return true if the val is contained in the BST, false otherwise."""
        return self._contains(value, self.root)

    def _contains(self, value, node):
        if node.value == value:
            return True
        elif value > node.value:
            if node.right_child:
                return self._contains(value, node.right_child)
            else:
                return False
        else:
            if node.left_child:
                return self._contains(value, node.left_child)
            else:
                return False

    def balance(self):
        """Return negative number if left leaning, postive for right leaning, or zero for balanced."""
        if self.root:
            right = self._depth(self.root.right_child)
            left = self._depth(self.root.left_child)
            return right - left
        return 0


if __name__ == "__main__":
    """Calculate the runtime for binary searches in the BST."""
    import timeit
    value = [50, 45, 60, 58, 59, 55, 70, 75, 65, 20, 48, 49, 46, 10, 25]
    balanced = BST(value)
    unbalanced = BST(sorted(value))

    bal = timeit.timeit(
        stmt="balanced.search(75)",
        setup="from __main__ import balanced",
        number=1000
    ) * 1000
    unbal = timeit.timeit(
        stmt="unbalanced.search(75)",
        setup="from __main__ import unbalanced",
        number=1000
    ) * 1000
    print("It takes {} microseconds to find 75 in a balanced tree, and {} microseconds to find 75 in an unbalanced tree".format(bal, unbal))
