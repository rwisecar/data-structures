"""Create a Doubly linked list."""


class Node(object):
    """Create node to push into Doubly link list."""

    def __init__(self, value=None, next_node=None, previous_node=None):
        """Create node to push into Doubly link list."""
        self.value = value
        self.next_node = next_node
        self.previous_node = previous_node
