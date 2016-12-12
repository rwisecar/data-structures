"""Test for linked_list.py module."""

import pytest


def test_create_node():
    """Test whether we create a node with a value 'val'."""
    from linked_list import Node
    test_node = Node(15)
    assert test_node.val == 15


def test_create_list():
    """Test whether we create a new Linked List instance."""
    from linked_list import Node
    from linked_list import LinkedList
    new_node = Node(val=15, next=None)
    new_list = LinkedList(head=new_node, length=15)
    assert new_list.head == new_node and new_list.length == 15
