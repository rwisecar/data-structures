"""Tests for graph module."""

import pytest

@pytest.fixture
def new_graph():
    """Create a new graph."""
    from graph import Graph
    this_graph = Graph()
    return this_graph

def test_a_graph_exists(new_graph):
    """Test to make sure graph instantiates."""
    assert new_graph.graph == {}


def test_adding_node(new_graph):
    """Test added node exists."""
    new_graph.add_node("Wisecarver, Rachael")
    assert "Wisecarver, Rachael" in new_graph.graph.keys()


def test_add_existing_node(new_graph):
    """Test you can't add an existing node."""
    new_graph.add_node("Wisecarver, Rachael")
    with pytest.raises(KeyError):
        new_graph.add_node("Wisecarver, Rachael")


def test_add_edge_will_create_node(new_graph):
    """Test add_edge() will create node(s)."""
    new_graph.add_edge("Wisecarver, Rachael", "Valenzuela, Rick")
    assert "Wisecarver, Rachael" in new_graph.graph.keys()
    assert "Valenzuela, Rick" in new_graph.graph.keys()

