"""An implementation of a trie."""


class TrieNode(object):
    """Create node to for use in a trie tree."""

    def __init__(self, value=None):
        """Create node to push into Doubly link list."""
        self.value = value
        self.children = {}


class Trie(object):
    """An implementation of a trie tree.

    insert(self, string): will insert the input string into the trie. If character in the input string is already present, it will be ignored.

    contains(self, string): will return True if the string is in the trie, False if not.

    size(self): will return the total number of words contained within the trie. 0 if empty.

    remove(self, string): will remove the given string from the trie. If the word does not exist, will raise an appropriate exception.
    """

    def __init__(self):
        """Initialize a trie tree."""
        self.root = TrieNode()
        self._size = 0

    def insert(self, string):
        """Insert a string into the trie."""
        if not isinstance(string, str):
            raise TypeError("Word must be a string")
        current = self.root
        word_progression = ''
        for letter in string:
            word_progression += letter
            if letter in current.children:
                current = current.children[letter]
            else:
                current.children[letter] = TrieNode(word_progression)
                current = current.children[letter]
        current.children['$'] = string
        self._size += 1

    def contains(self, string):
        """Return true if string is in trie."""
        current = self.root
        for letter in string:
            if letter in current.children:
                current = current.children[letter]
            else:
                return False
        try:
            if current.children['$']:
                return True
        except KeyError:
            raise KeyError("That word has not been inserted")

    def size(self):
        """Return the number of words contained in the trie."""
        return self._size

    def remove(self, string):
        """Return the string from the trie if it exists."""
        pass
