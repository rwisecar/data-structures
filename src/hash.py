"""Create a hashtable."""


class Hash(object):
    """Create a hashtable. Its functions are as follows.
    get(key) - should return the value stored with the given key.
    set(key, val) - should store the given val using the given key.
    _hash(key) - should hash the key provided.
    """

    def __init__(self, size):
        """Instantiates hashtable instance."""
        self._size = size
        self._hashtable = [[] for n in range(size)]

    def set(self, key, value):
        """Store the given value using the given key."""
        if type(key) is not str:
            raise TypeError("Hash tables can only accept strings.")
        key_hash = self._hash(key)
        bucket = self._hashtable[key_hash]
        if bucket:
            for tup in bucket:
                if tup[0] == key:
                    bucket.remove(tup)
        self._hashtable[key_hash].append((key, value))

    def _hash(self, key):
        """Hash the key provided."""
        nums = sum([ord(k) for k in key])
        return nums % self._size

    def get(self, key):
        """Return the value stored with the given key."""
        key_hash = self._hash(key)
        bucket = self._hashtable[key_hash]
        for tup in bucket:
            if tup[0] == key:
                return tup[1]
