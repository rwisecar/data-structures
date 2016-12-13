"""Test for linked_list.py module."""

import pytest
from linked_list import Node, LinkedList


def test_create_node():
    """Test whether we create a node with a value 'val'."""
    test_node = Node(15)
    assert test_node.data == 15


def test_create_list():
    """Test whether we create a new Linked List instance."""
    new_node = Node(data=15, next_node=None)
    new_list = LinkedList(head=new_node, data=None, length=1)
    assert new_list.head == new_node and new_list.length == 1


def test_create_from_existing_list():
    """Test whether we can create a linked list from an existing list."""
    new_list = LinkedList(head=None, data=[1, 2, 3], length=3)
    new_node = Node(data=3)
    assert new_list.head.data == new_node.data


def test_size():
    """Test whether length of the link link"""
    linked_list1 = LinkedList(head=2, length=10)
    assert linked_list1.size() == linked_list1.length


def test_push():
    """Test whether the push method adds a node to the end."""
    node1 = Node(15)
    node2 = Node(10)
    new_list = LinkedList(head=node1, data=None, length=1)
    new_list.push(node2)
    assert new_list.length == 2


def test_pop():
    """Test whether the pop method removes and returns the first node."""
    node1 = Node(15)
    node2 = Node(10)
    node3 = Node(5)
    new_list = LinkedList(node1, length=1)
    new_list.push(node2)
    new_list.push(node3)
    assert new_list.pop().data == node3.data


def test_pop_length():
    """Test whether the length of the list changes when a value is popped."""
    new_list = LinkedList(data=[5, 10, 15], length=3)
    new_list.pop()
    assert new_list.length == 2


def test_search():
    """Test whether the search method returns the correct value."""
    new_list = LinkedList(data=[5, 10, 15], length=3)
    assert new_list.search(10).data == 10


def test_display():
    """Test that the display method returns a stringified tuple of the list."""
    new_list = LinkedList(data=[5, 10, 15, 20], length=4)
    new_list.display() == "(20, 15, 10, 5)"


# def test_remove_length():
#     """Test whether the length of the list changes when you remove a value."""
#     node1 = Node(15)
#     node2 = Node(10)
#     node3 = Node(5)
#     new_list = LinkedList(node1, length=1)
#     new_list.push(node2)
#     new_list.push(node3)
#     new_list.remove(node2)
#     assert new_list.length == 2
