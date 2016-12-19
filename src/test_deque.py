"""Test deque.py."""

import pytest

@pytest.fixture
def empty_deque():
    """Create empty deque."""
    from deque import Deque
    unpopulated_deque = Deque()
    return unpopulated_deque


@pytest.fixture
def full_deque():
    """Create deque initialized with iterable."""
    from deque import Deque
    populated_deque = Deque(iterable=[1, 2, 3])
    return populated_deque


def test_full_deque_is_full(full_deque):
    """Test that populating deque with iterable produces head with value of 3."""
    assert full_deque._deque.head.value == 3


def test_full_deque_has_tail(full_deque):
    """Test that populating deque with iterable has correct tail element."""
    assert full_deque._deque.tail.value == 1


def test_full_deque_has_length(full_deque):
    """Test that full deque has length of 3."""
    assert full_deque._deque._length == 3


def test_empty_deque_is_empty(empty_deque):
    """Test that empty deque is empty."""
    assert empty_deque.size() == 0


def test_initializing_deque_with_non_iterable_raises_error():
    """Test that error is raised when you try to initialize with noniterable."""
    from deque import Deque
    with pytest.raises(TypeError):
        new_deque = Deque(interable=123456)


def test_append_to_empty_deque_check_head(empty_deque):
    empty_deque.append("Denny Way")
    assert empty_deque._deque.head.value == "Denny Way"


def test_append_to_empty_deque_check_tail(empty_deque):
    empty_deque.append("Denny Way")
    assert empty_deque._deque.tail.value == "Denny Way"


def test_append_to_empty_deque_size(empty_deque):
    empty_deque.append("Denny Way")
    assert empty_deque.size() == 1


def test_append_to_full_deque_check_head(full_deque):
    full_deque.append("Denny Way")
    assert full_deque._deque.head.value == 3


def test_append_to_full_deque_check_tail(full_deque):
    full_deque.append("Denny Way")
    assert full_deque._deque.tail.value == "Denny Way"


def test_append_to_full_deque_size(full_deque):
    full_deque.append("Denny Way")
    assert full_deque.size() == 4


