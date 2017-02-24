import pandas


class DecisionTree(object):
    """Class for decision tree implementation.

    clf.fit(self, data): construct a decision tree based on some incoming data set; returns nothing
    clf.predict(self, data): returns labels for your test data.

    """

    def __init__(self, iterable, max_depth=None, min_leaf_size=None):
        """Initialize decision tree."""
        self.iterable = iterable
        self.max_depth = max_depth
        self.min_leaf_size = min_leaf_size
        self._depth = 0

    def fit(self, data):
        """Construct a decision tree based on data."""
        pass

    def predict(self, data):
        """Return label for data."""
        pass
