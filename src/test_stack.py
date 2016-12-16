"""Test stack.py"""

import pytest


@pytest.fixture
def new_stack():
    """Create a new stack with some data as a fixture."""
    from stack import Stack
    this_stack = Stack(data=[1, 2, 3])
    return this_stack


def test_new_stack_is_empty():
    """Check that a new stack is empty."""
    from stack import Stack
    this_stack = Stack()
    assert this_stack._linkedlist.length == 0


def test_new_stack_with_data_has_data(new_stack):
    """Check new stack with has data."""
    assert new_stack._linkedlist.head.value == 3


def test_new_stack_with_head_has_head():
    """Check new stack with head kwarg has head."""
    from stack import Stack
    this_stack = Stack(5)
    assert this_stack._linkedlist.head.value == 5


def test_pushed_value_is_new_head(new_stack):
    """When pushing to stack, the pushed value should be the new head."""
    new_stack.push("new")
    assert new_stack._linkedlist.head.value == "new"


def test_length_of_stack(new_stack):
    """Check that size of the stack reflects the number of nodes in the stack."""
    assert new_stack._linkedlist.length == 3


def test_length_of_stack_when_pushed(new_stack):
    """Check that size changes to reflect pushed values."""
    new_stack.push("new")
    assert new_stack._linkedlist.length == 4


def test_size_of_stack_with_nodes(new_stack):
    """Check that the size of a nonempty stack is accurate."""
    assert new_stack._linkedlist.length == 3


def test_length_of_stack_when_popped(new_stack):
    """Check that size decreases when popped."""
    new_stack.pop()
    assert new_stack._linkedlist.length == 2


def test_pop_with_values():
    """Check that pop removes the top value from the stack."""
    from stack import Stack
    this_stack = Stack(data=[1, 2, 3])
    assert this_stack.pop() == 3


def test_pop_without_values():
    """Check that pop raises IndexError when called on empty stack."""
    from stack import Stack
    this_stack = Stack()
    with pytest.raises(IndexError):
        this_stack.pop()
