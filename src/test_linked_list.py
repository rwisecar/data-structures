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

def test_create_size():
    """Test whether length of the link link"""
    from linked_list import LinkedList
    linked_list1 = LinkedList(head=2, length=10)
    assert linked_list1.size() == linked_list1.length

def test_create_push():
    from linked_list import Node, LinkedList
    node1 = Node(15)
    node2 = Node(10)
    new_list = LinkedList(node1, length=1)
    new_list.push(node2)
    assert new_list.length==2




    
