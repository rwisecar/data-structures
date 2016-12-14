"""Test for test_dll.py module."""

import pytest
from dll import Node


def test_create_node():
    """Test whether we create a node with a value 'val'."""
    test_node = Node(15)
    assert test_node.value == 15


def test_create_empty_node():
    """Test whether we create a node with a value 'val'."""
    test_node = Node()
    assert test_node.value is None


def test_test_next_node():
    """Test whether creating a next with another node."""
    test_node1 = Node(15)
    test_node2 = Node(10, next_node=test_node1)
    assert test_node2.next_node.value == 15


def test_test_previous_node():
    """Test whether creating a previous with another previous node."""
    test_node2 = Node(10)
    test_node1 = Node(20, previous_node=test_node2)
    assert test_node1.previous_node.value == 10
