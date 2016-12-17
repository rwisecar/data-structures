"""Test for test_dll.py module."""

import pytest
from dll import Node, DoubleLink


@pytest.fixture
def full_list():
    new_list = DoubleLink(iterable=[1, 2, 3])
    return new_list


def test_create_node():
    """Test whether we create a node with a value 'val'."""
    test_node = Node(15)
    assert test_node.value == 15


def test_create_empty_node():
    """Test whether we create a node with a value 'val'."""
    test_node = Node()
    assert test_node.value is None


def test_create_list_raise_error():
    """Test that TypeError is raised when you init with noniterable."""
    with pytest.raises(TypeError):
        new_dll = DoubleLink(iterable=123456)


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


def test_create_empty_dll():
    """Test whether we create an empty list."""
    new_list = DoubleLink()
    assert new_list._length is 0


def test_create_one_value_list():
    """Test that you can create list with one value."""
    new_list = DoubleLink(1)
    assert new_list._length == 1


def test_create_multi_value_list(full_list):
    """Test that you can create list with iterable."""
    assert full_list._length == 3


def test_push_new_node_to_full_dll(full_list):
    """Test that you can push a new value to a nonempty list."""
    full_list.push(15)
    assert full_list.head.value == 15


def test_push_next_node(full_list):
    """Test that when you push to a nonempty list, the next node is previous head."""
    full_list.push(15)
    assert full_list.head.next_node.value == 3


def test_push_previous_node(full_list):
    """Test that when you push to a nonempty list, the next node's previous node is the head."""
    full_list.push(15)
    assert full_list.head.next_node.previous_node.value == 15


def test_push_tail_node_empty_list():
    """Test that when you push to an empty list, the head is also the tail."""
    new_list = DoubleLink()
    new_list.push(15)
    assert new_list.tail.value == 15


def test_push_tail_node_full_list(full_list):
    """Test that the tail node is the last node when you make a list."""
    assert full_list.tail.value == 1


def test_size_of_stack_when_pushed(full_list):
    """Check for decreasing size when popped."""
    full_list.pop()
    assert full_list._length == 2


def test_pop_with_value(full_list):
    """Checking for pop from the value."""
    full_list.pop()
    assert full_list.head.value == 2


def test_pop_without_values():
    """Check index error when called empty list."""
    full_list = DoubleLink()
    with pytest.raises(IndexError):
        full_list.pop()


def test_append_adds_value(full_list):
    """Check that append adds a value to the end of the list."""
    full_list.append(15)
    assert full_list.tail.value == 15


def test_append_empty_list():
    """Check that append adds a value to an empty list."""
    new_list = DoubleLink()
    new_list.append(15)
    assert new_list.tail.value == 15


def test_append_length_list(full_list):
    """Check that list length extends when you append value."""
    full_list.append(15)
    assert full_list._length == 4


def test_shift_last_value(full_list):
    """Check that second to last list value is new tail."""
    full_list.shift()
    assert full_list.tail.value == 2


def test_shift_without_values():
    """Check index error when called empty list."""
    full_list = DoubleLink()
    with pytest.raises(IndexError):
        full_list.shift()


def test_shift_length(full_list):
    """Check that list length changes when you shift."""
    full_list.shift()
    assert full_list._length == 2


def test_remove_length(full_list):
    """Check that list length decreases when you remove value."""
    full_list.remove(2)
    assert full_list._length == 2


def test_remove_head(full_list):
    """Check that when you remove the head, it pops and resets the head."""
    full_list.remove(3)
    assert full_list.head.value == 2


def test_remove_value(full_list):
    """Check that when you remove a value, that value is actually removed."""
    full_list.remove(2)
    assert full_list.head.next_node.value == 1


# def test_raise_value_error(full_list):
#     """Check that when you search for value that DNE, return ValueError."""
#     with pytest.raises(ValueError):
#         full_list.remove(15)





