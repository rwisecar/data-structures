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
