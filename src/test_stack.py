"""Test stack.py"""

import pytest


def test_new_stack_is_empty():
    """Check that a new stack is empty."""
    from stack import Stack
    this_stack = Stack()
    assert this_stack._linkedlist.size() == 0


def test_new_list_has_zero_size():
    """Check that a new list has no size."""
    from stack import Stack
    this_stack = Stack()
    assert this_stack._linkedlist.size() == 0


def test_new_stack_with_data_has_data():
    """Check new stack with has data."""
    from stack import Stack
    this_stack = Stack(data=[1, 2, 3])
    assert this_stack._linkedlist.head.value == 3


def test_new_stack_with_head_has_head():
    """Check new stack with head kwarg has head."""
    from stack import Stack
    from linked_list import Node
    node1 = Node(5)
    this_stack = Stack(head=node1)
    assert this_stack._linkedlist.head.value == 5


def test_pushed_value_is_new_head():
    """When pushing to stack, the pushed value should be the new head."""
    from stack import Stack
    this_stack = Stack(data=[1, 2, 3])
    this_stack._linkedlist.push("new")
    assert this_stack._linkedlist.head.value == "new"


def test_length_of_stack():
    """Check that size of the stack reflects the number of nodes in the stack."""
    from stack import Stack
    this_stack = Stack(data=[1, 2, 3])
    assert this_stack._linkedlist.length == 3


def test_length_of_stack_when_pushed():
    """Check that size changes to reflect pushed values."""
    from stack import Stack
    this_stack = Stack(data=[1, 2, 3])
    this_stack._linkedlist.push("new")
    assert this_stack._linkedlist.length == 4


def test_size_of_stack_with_nodes():
    """Check that the size of a nonempty stack is accurate."""
    from stack import Stack
    this_stack = Stack(data=[1, 2, 3])
    assert this_stack._linkedlist.size() == 3


def test_size_of_stack_when_pushed():
    """Check that size changes to reflect pushed values."""
    from stack import Stack
    this_stack = Stack(data=[1, 2, 3])
    this_stack._linkedlist.push("new")
    assert this_stack._linkedlist.size() == 4


def test_size_of_stack_when_popped():
    """Check that size decreases when popped."""
    from stack import Stack
    this_stack = Stack(data=[1, 2, 3])
    this_stack._linkedlist.pop()
    assert this_stack._linkedlist.size() == 2


def test_pop_with_values():
    """Check that pop removes the top value from the stack."""
    from stack import Stack
    this_stack = Stack(data=[1, 2, 3])
    assert this_stack._linkedlist.pop() == 3


def test_pop_without_values():
    """Check that pop raises IndexError when called on empty stack."""
    from stack import Stack
    this_stack = Stack()
    with pytest.raises(IndexError):
        this_stack._linkedlist.pop()
