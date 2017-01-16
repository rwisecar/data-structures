"""Tests for graph module."""

import pytest

EDGES_TABLE = [
    ['Wisecarver, Rachael', 'Valenzuela, Rick'],
    []
]


@pytest.fixture
def empty_graph():
    """Fixture for an instantiated but empty graph."""
    from graph import Graph
    this_graph = Graph()
    return this_graph


@pytest.fixture
def three_node_graph():
    """Fixture for a graph with three nodes."""
    from graph import Graph
    this_graph = Graph()
    this_graph.add_node("Wisecarver, Rachael")
    this_graph.add_node("Valenzuela, Rick")
    this_graph.add_node("Hunt-Walker, Nicholas")
    return this_graph


@pytest.fixture
def graph_with_edges():
    """Fixture for a graph with edges."""
    from graph import Graph
    new_graph = Graph()
    new_graph.add_node(5)
    new_graph.add_edge(5, 10, 3)
    new_graph.add_edge(5, 15, 6)
    new_graph.add_edge(10, 15, 2)
    return new_graph


@pytest.fixture
def bigger_graph_with_edges():
    """Fixture for a graph with edges. Bigger than before."""
    from graph import Graph
    new_graph = Graph()
    new_graph.add_node(5)
    new_graph.add_edge(5, 10, 2)
    new_graph.add_edge(5, 15, 4)
    new_graph.add_edge(10, 15, 6)
    new_graph.add_edge(10, 9, 8)
    new_graph.add_edge(9, 11, 10)
    return new_graph


@pytest.fixture
def circular_graph():
    """Fixture for a graph with edges."""
    from graph import Graph
    new_graph = Graph()
    new_graph.add_node(5)
    new_graph.add_edge(5, 10, 2)
    new_graph.add_edge(10, 15, 4)
    new_graph.add_edge(15, 5, 6)
    return new_graph


def test_a_graph_exists(empty_graph):
    """Test to make sure graph instantiates."""
    assert empty_graph.graph == {}


def test_adding_node(empty_graph):
    """Test added node exists."""
    empty_graph.add_node("Wisecarver, Rachael")
    assert "Wisecarver, Rachael" in empty_graph.graph.keys()


def test_add_existing_node(empty_graph):
    """Test you can't add an existing node."""
    empty_graph.add_node("Wisecarver, Rachael")
    with pytest.raises(KeyError):
        empty_graph.add_node("Wisecarver, Rachael")


def test_add_edge_will_create_node(empty_graph):
    """Test add_edge() will create nodes in empty graph."""
    empty_graph.add_edge("Wisecarver, Rachael", "Valenzuela, Rick", 10)
    assert "Wisecarver, Rachael" in empty_graph.graph.keys()
    assert "Valenzuela, Rick" in empty_graph.graph.keys()


def test_add_edge_when_first_node_doesnt_exist(empty_graph):
    """Test add_edge() creates nonexistent first node/argument."""
    empty_graph.add_node("Wisecarver, Rachael")
    empty_graph.add_edge("Valenzuela, Rick", "Wisecarver, Rachael", 10)
    assert "Valenzuela, Rick" in empty_graph.graph.keys()


def test_add_edge_when_second_node_doesnt_exist(empty_graph):
    """Test add_edge() creates nonexistent second node/argument."""
    empty_graph.add_node("Wisecarver, Rachael")
    empty_graph.add_edge("Wisecarver, Rachael", "Valenzuela, Rick", 10)
    assert "Valenzuela, Rick" in empty_graph.graph.keys()


def test_add_edge_creates_edge(empty_graph):
    """Test add_edge() adds edge."""
    empty_graph.add_edge("Wisecarver, Rachael", "Valenzuela, Rick", 10)
    assert empty_graph.graph["Wisecarver, Rachael"]["Valenzuela, Rick"] == 10


def test_add_edge_only_in_expected_direction(empty_graph):
    """Test add_edge() doesn't add edge in reverse director."""
    empty_graph.add_edge("Wisecarver, Rachael", "Valenzuela, Rick", 10)
    assert "Elvis" not in empty_graph.graph[
        "Wisecarver, Rachael"]


def test_nodes_list_on_empty_graph(empty_graph):
    """Test that nodes() returns an empty list when run on empty graph."""
    assert empty_graph.nodes() == []


def test_nodes_lists_nodes(three_node_graph):
    """Test nodes() lists all nodes in graph."""
    assert "Valenzuela, Rick" in three_node_graph.graph.keys()
    assert "Wisecarver, Rachael" in three_node_graph.graph.keys()
    assert "Hunt-Walker, Nicholas" in three_node_graph.graph.keys()


def test_nodes_list_length_grows_with_new_node(three_node_graph):
    """Test the length of nodes_list changes when you add node."""
    three_node_graph.add_node("15")
    assert len(three_node_graph.graph) == 4


def test_nodes_list_add_node_check_if_value_in_list(three_node_graph):
    """Test the length of nodes_list changes when you add node."""
    three_node_graph.add_node(15)
    assert 15 in three_node_graph.graph.keys()


def test_nodes_list_append_node(empty_graph):
    """Test that nodes list appends a node."""
    empty_graph.add_node(5)
    empty_graph.nodes()
    assert 5 in empty_graph.graph.keys()


def test_edges_list_returns_list_of_edges(graph_with_edges):
    """Test that running edges returns a list of edges."""
    assert graph_with_edges.edges() == ['10: [15]', '5: [10, 15]', '15: []']


def test_edges_list_with_no_edges(three_node_graph):
    """Test that you get a list with no edges where no edges."""
    assert "Valenzuela, Rick: []" in three_node_graph.edges()
    assert "Wisecarver, Rachael: []" in three_node_graph.edges()
    assert "Hunt-Walker, Nicholas: []" in three_node_graph.edges()


def test_edges_list_with_new_keys(empty_graph):
    """Test that edges returns an empty list when run on an empty graph."""
    assert empty_graph.edges() == []


def test_del_node_deletes_node(three_node_graph):
    """Test that del_node actually deletes the node."""
    three_node_graph.del_node("Wisecarver, Rachael")
    assert ("Wisecarver, Rachael") not in three_node_graph.graph.keys()


def test_del_node_changes_length(three_node_graph):
    """Test that del_node actually deletes the node."""
    three_node_graph.del_node("Wisecarver, Rachael")
    assert len(three_node_graph.graph) == 2


def test_del_node_when_node_does_not_exist(three_node_graph):
    """Test that del_node raises a Key Error if the node DNE."""
    with pytest.raises(KeyError):
        three_node_graph.del_node("Ford, Harrison")


def test_del_node_removes_edges_to_node_in_other_nodes(graph_with_edges):
    """Test that del_node removes references to n in other nodes."""
    graph_with_edges.del_node(15)
    assert 15 not in graph_with_edges.graph[5].keys()
    assert 15 not in graph_with_edges.graph[10].keys()


def test_del_edge_raises_error_when_no_edge(graph_with_edges):
    """Test that ValueError is raised when edge not in graph."""
    with pytest.raises(ValueError):
        graph_with_edges.del_edge(10, 5)


def test_edge_deletes_edge(graph_with_edges):
    """Test that del_edge deletes the edge from the graph."""
    graph_with_edges.del_edge(5, 10)
    assert 10 not in graph_with_edges.graph[5].keys()


def test_del_edge_raises_keyerror_if_n1_not_in_graph(graph_with_edges):
    """Test that a KeyError is raised if n1 is not in the graph."""
    with pytest.raises(KeyError):
        graph_with_edges.del_edge(100, 5)


def test_del_edge_raises_keyerror_if_n2_not_in_graph(graph_with_edges):
    """Test that a KeyError is raised if n2 is not in the graph."""
    with pytest.raises(KeyError):
        graph_with_edges.del_edge(5, 100)


def test_has_node_haz_nodez(three_node_graph):
    """Test known node is indeed in graph."""
    assert three_node_graph.has_node("Hunt-Walker, Nicholas") is True


def test_has_node_when_node_nonexistent(three_node_graph):
    """Test that False returned when nonexistent node called."""
    assert three_node_graph.has_node("Elvis Presley") is False


def test_neighbors_with_nonexistent_node(empty_graph):
    """Test error raised when asking for neighbors of nonexisting node."""
    with pytest.raises(KeyError):
        empty_graph.neighbors("Coffee Mug")


def test_neighbors_lists_arguments_edges(graph_with_edges):
    """Test method returns edges for given node."""
    assert graph_with_edges.neighbors(5) == {10: 3, 15: 6}


def test_neighbors_when_no_neighbors(graph_with_edges):
    """Test that neighbors returns empty list when node has no neighbors."""
    assert graph_with_edges.neighbors(15) == {}


def test_adjacent_returns_true_on_edge(graph_with_edges):
    """Test adjacent() returns True when edge exists."""
    assert graph_with_edges.adjacent(5, 10) is True


def test_adjacent_raises_error_on_nonexistent_n2(graph_with_edges):
    """Test error is raised when one of key args isn't in graph."""
    with pytest.raises(KeyError):
        graph_with_edges.adjacent(5, "Charlie Brown")


def test_adjacent_raises_error_on_nonexistent_n1(graph_with_edges):
    """Test error is raised when one of key args isn't in graph."""
    with pytest.raises(KeyError):
        graph_with_edges.adjacent("Charlie Brown", 5)


def test_adjacent_for_lack_of_connection(graph_with_edges):
    """Test should return False for no connection."""
    graph_with_edges.add_node("Charlie Brown")
    assert graph_with_edges.adjacent(15, "Charlie Brown") is False


def test_depth_traversal_for_unknown_node(graph_with_edges):
    """Test depth traversal with starting point not in graph."""
    with pytest.raises(KeyError):
        graph_with_edges.depth_traversal("backpack")


def test_depth_traversal_returns_expected_path(graph_with_edges):
    """Test DFS returns expected path through graph."""
    assert graph_with_edges.depth_traversal(5) == [5, 10, 15]


def test_depth_traversal_nonsequential_path(bigger_graph_with_edges):
    """Test BFS returns expected path that's not in sequential order."""
    assert bigger_graph_with_edges.depth_traversal(5) == [
        5, 10, 9, 11, 15] or bigger_graph_with_edges.depth_traversal(5) == [
        5, 10, 15, 9, 11]


def test_depth_traversal_circular_graph_not_looping(circular_graph):
    """Test DFS on circuitous path doesn't loop."""
    assert circular_graph.depth_traversal(5) == [5, 10, 15]


def test_depth_traversal_for_unconnected_node(graph_with_edges):
    """Test that node with no edges doesn't end up in path."""
    graph_with_edges.add_node(23)
    assert graph_with_edges.depth_traversal(5) == [5, 10, 15]


def test_breadth_traversal_for_unknown_node(graph_with_edges):
    """Test breadth traversal with starting point not in graph."""
    with pytest.raises(KeyError):
        graph_with_edges.breadth_traversal("backpack")


def test_breadth_traversal_returns_expected_path(graph_with_edges):
    """Test BFS returns expected path through graph."""
    assert graph_with_edges.breadth_traversal(5) == [5, 10, 15]


def test_breadth_traversal_nonsequential_path(bigger_graph_with_edges):
    """Test BFS returns expected path that's not in sequential order."""
    assert bigger_graph_with_edges.breadth_traversal(5) == [
        5, 10, 15, 9, 11]


def test_breadth_traversal_circular_graph_not_looping(circular_graph):
    """Test bFS on circuitous path doesn't loop."""
    assert circular_graph.breadth_traversal(5) == [5, 10, 15]


def test_breadth_traversal_for_unconnected_node(graph_with_edges):
    """Test that node with no edges doesn't end up in path."""
    graph_with_edges.add_node(23)
    assert graph_with_edges.breadth_traversal(5) == [5, 10, 15]


def test_added_edge_shows_weight(graph_with_edges):
    """Make sure edge is weighted."""
    graph_with_edges.graph[10] == {15: 2}
