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
def three_node_graph_with_edges():
    """Fixture for a graph with three nodes."""
    from graph import Graph
    this_graph = Graph()
    empty_graph.add_node("Wisecarver, Rachael")
    empty_graph.add_node("Valenzuela, Rick")
    empty_graph.add_node("Hunt-Walker, Nicholas")
    return this_graph


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
    empty_graph.add_edge("Wisecarver, Rachael", "Valenzuela, Rick")
    assert "Wisecarver, Rachael" in empty_graph.graph.keys()
    assert "Valenzuela, Rick" in empty_graph.graph.keys()


def test_add_edge_when_first_node_doesnt_exist(empty_graph):
    """Test add_edge() creates nonexistent first node/argument."""
    empty_graph.add_node("Wisecarver, Rachael")
    empty_graph.add_edge("Valenzuela, Rick", "Wisecarver, Rachael")
    assert "Valenzuela, Rick" in empty_graph.graph.keys()


def test_add_edge_when_second_node_doesnt_exist(empty_graph):
    """Test add_edge() creates nonexistent second node/argument."""
    empty_graph.add_node("Wisecarver, Rachael")
    empty_graph.add_edge("Wisecarver, Rachael", "Valenzuela, Rick")
    assert "Valenzuela, Rick" in empty_graph.graph.keys()


def test_add_edge_creates_edge(empty_graph):
    """Test add_edge() adds edge."""
    empty_graph.add_edge("Wisecarver, Rachael", "Valenzuela, Rick")
    assert empty_graph.graph["Wisecarver, Rachael"]["edges"] == ["Valenzuela, Rick"]

