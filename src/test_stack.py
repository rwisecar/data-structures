"""Test stack.py"""

import pytest


# @pytest.fixture
# def new_stack():
#     from stack import Stack
#     this_stack = Stack()
#     return this_stack


def test_new_stack_is_empty():
    """Check that a new stack is empty."""
    from stack import Stack
    this_stack = Stack()
    assert this_stack._linkedlist.size() == 0
