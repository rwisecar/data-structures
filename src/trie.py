"""An implementation of a trie."""


class TrieNode(object):
    """Create node to for use in a trie tree."""

    def __init__(self, value=None):
        """Create node to push into Doubly link list."""
        self.value = value
        self.children = {}


class Trie(object):
    """An implementation of a trie tree."""

    def __init__(self):
        self.root = TrieNode()

