"""Create an unweighted, directed graph."""


class Graph():
    """
    Create an unweighted, directed graph instance with the following methods.

    nodes(): returns a list of all nodes in the graph.

    edges(): returns a list of all edges in the graph.

    add_node(n): adds a new node, n, to the graph.

    add_edge(n1, n2): adds n1 and n2 if they don't exist, and adds an edge connecting them.

    del_node(n): deletes node n from the graph.

    del_edge(n1, n2): deletes the edge connecting n1 and n2.

    has_node(n): Returns True if node n is contained in the graph.

    neighbors(n): Returns a list of all nodes connected to n by edges.

    adjacent(n1, n2): returns True if n1 and n2 are connceted by an edge.
    """

    def __init__(self):
        """Instantiates a new graph instance."""
        self.graph = {}

    def add_node(self, n):
        """Adds a node to the graph."""
        self.graph[n] = {"edges": {}}

    def add_edge(self, n1, n2):
        """Add an edge between two nodes in the graph."""
        pass