"""Create a hashtable."""


class Hash(object):
    """Create a hashtable. Its functions are as follows.
    get(key) - should return the value stored with the given key.
    set(key, val) - should store the given val using the given key.
    _hash(key) - should hash the key provided.
    """

    def __init__(self, size):
        """Instantiates hashtable instance."""
        self._hashtable = [[] for n in range(size)]

    
