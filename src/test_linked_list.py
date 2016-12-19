"""Test for linked_list.py module."""

import pytest
from linked_list import Node, LinkedList


@pytest.fixture
def empty_list():
    """Create an empty list fixture."""
    from linked_list import LinkedList
    new_list = LinkedList()
    return new_list


@pytest.fixture
def full_list():
    """Create a full list via fixture."""
    from linked_list import LinkedList
    full_list = LinkedList(data=[1, 2, 3])
    return full_list


def test_create_node():
    """Test whether we create a node with a value 'val'."""
    test_node = Node(15)
    assert test_node.value == 15


def test_create_empty_list(empty_list):
    """Test whether we create an empty new Linked List instance."""
    assert empty_list.length == 0


def test_create_list_with_head():
    """Test whether we can create a list with an input head."""
    new_list = LinkedList(15)
    assert new_list.length == 1


def test_create_list_with_data(full_list):
    """Test whether we can create a linked list from an existing list."""
    assert full_list.head.value == 3


def test_create_list_raise_error():
    """Test that TypeError is raised when you call list with noniterable."""
    with pytest.raises(TypeError):
        data_list = LinkedList(data=123456)


def test_size():
    """Test whether length of the link link"""
    linked_list1 = LinkedList(2)
    assert linked_list1.size() == linked_list1.length


def test_push():
    """Test whether the push method adds a node to the head."""
    new_list = LinkedList()
    new_list.push(15)
    assert new_list.head.value == 15


def test_push_to_full_list(full_list):
    """Test whether head us expected node when you push to full list."""
    full_list.push(15)
    assert full_list.head.value == 15


def test_pop(full_list):
    """Test whether the pop method removes and returns the first node."""
    assert full_list.pop() == 3


def test_pop_length(full_list):
    """Test whether the length of the list changes when a value is popped."""
    full_list.pop()
    assert full_list.length == 2


def test_search(full_list):
    """Test whether the search method returns the correct value."""
    assert full_list.search(2) == 2


def test_search_value_error(full_list):
    """Test whether search of value not in list raises error."""
    with pytest.raises(ValueError):
        full_list.search("hello")


def test_display(full_list):
    """Test that the display method returns a stringified tuple of the list."""
    full_list.display() == "(3, 2, 1)"


def test_remove_length(full_list):
    """Test whether the length of the list changes when you remove a value."""
    full_list.remove(2)
    assert full_list.length == 2


def test_remove_next_node(full_list):
    """Check that when you remove a node, its value is gone."""
    full_list.remove(2)
    assert full_list.head.next_node.value == 1


def test_remove_head(full_list):
    """Test that remove works on the head of the list."""
    full_list.remove(3)
    assert full_list.head.value == 2


def test_remove_value_error(full_list):
    """Check that removing a value not in list returns error."""
    with pytest.raises(ValueError):
        full_list.remove("hello")

