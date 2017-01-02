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
        """Instantiate a new graph instance."""
        self.graph = {}

    def add_node(self, n):
        """Add a node to the graph."""
        if n in self.graph.keys():
            raise KeyError("Node already in graph.")
        self.graph[n] = {"edges": []}

    def add_edge(self, n1, n2):
        """Add an edge from n1 to n2 in the graph."""
        if n1 not in self.graph.keys():
            self.add_node(n1)
        if n2 not in self.graph.keys():
            self.add_node(n2)
        if n2 not in self.graph[n1]['edges']:
            self.graph[n1]['edges'].append(n2)

    def nodes(self):
        """Return a list of all nodes in the graph."""
        node_list = []
        for n in self.graph.keys():
            node_list.append(n)
        return node_list

    def edges(self):
        """Return a list of all edges in the graph."""
        edge_list = []
        # for item in self.graph.items():
        #     edge_list.append(item)
        for n in self.graph.keys():
            edge_list.append("{}: {}".format(n, self.graph[n]["edges"]))
        return edge_list

    def del_node(self, n):
        """Delete node n from the graph, raises error if does not exist."""
        if n not in self.graph.keys():
            raise KeyError("You can't delete a node that does not exist.")
        del self.graph[n]
        for key in self.graph.keys():
            if n in self.graph[key]["edges"]:
                self.graph[key]["edges"].remove(n)

    def del_edge(self, n1, n2):
        """Delete the edge connecting n1 and n2."""
        if self.graph[n1]['edges'] and self.graph[n2]:
            self.graph[n1]['edges'].remove(n2)
        elif n1 not in self.graph.keys() or n2 not in self.graph.keys():
            raise KeyError("That node is not in the graph.")
        else:
            raise ValueError("That edge is not in the graph.")

    def has_node(self, n):
        """Return True if node n is contained in the graph."""
        return n in self.graph.keys()

    def neighbors(self, n):
        """Return a list of all nodes connected to n by edges."""
        if n not in self.graph.keys():
            raise KeyError("Not in graph.")
        edges_list = []
        edges_list.extend(self.graph[n]['edges'])
        return edges_list

    def adjacent(self, n1, n2):
        """Return True if n1 and n2 are connected by an edge."""
        if n1 not in self.graph.keys():
            raise KeyError("{} is not in the graph.".format(n1))
        elif n2 not in self.graph.keys():
            raise KeyError("{} is not in the graph.".format(n2))
        return n1 in self.graph[n2]['edges'] or n2 in self.graph[n1]['edges']
