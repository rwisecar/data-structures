"""Tests for graph module."""

import pytest

# @pytest.fixture
# def new_

def test_a_graph_exists():
    """Test to make sure graph instantiates."""
    from graph import Graph
    new_graph = Graph()
    assert new_graph.graph == {}


def test_adding_node():
    """Test added node exists."""
    from graph import Graph
    new_graph = Graph()
    new_graph.add_node("Wisecarver, Rachael")
    assert "Wisecarver, Rachael" in new_graph.graph.keys()


def test_add_existing_node():
    """Test you can't add an existing node."""
    from graph import Graph
    new_graph = Graph()
    new_graph.add_node("Wisecarver, Rachael")
    with pytest.raises(KeyError):
        new_graph.add_node("Wisecarver, Rachael")
