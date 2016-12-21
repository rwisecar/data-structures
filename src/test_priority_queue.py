"""Tests for priority queue data structure."""

import pytest

@pytest.fixture
def empty_pqueue():
    """Fixture for empty priority queue."""
    from priority_queue import Priority_Q
    empty_prio_q = Priority_Q()
    return empty_prio_q


@pytest.fixture
def populated_pqueue():
    """Fixture for full heap."""
    from priority_queue import Priority_Q
    populated_q = Priority_Q([('Seattle', 1), ('Everett', 3), ('Tacoma', 5)])
    return populated_q


def test_cant_init_w_noniterable():
    """Test init doesn't work with non-iterable (insert handles tuple part)."""
    from priority_queue import Priority_Q
    with pytest.raises(TypeError):
        Priority_Q(8675309)


def test_initted_q_shows_q(populated_pqueue):
    """Test that populated, initialized queue shows data."""
    assert populated_pqueue._priorityq[2] == ('Tacoma', 5)


def test_insert_adds_to_q(empty_pqueue):
    """Test that inserted value is add."""
    empty_pqueue.insert(('Bellingham', 2))
    assert empty_pqueue[0] == ('Bellingham', 2)


def test_cant_pop_from_empty(empty_pqueue):
    """Test that pop raises error on empty queue."""
    with pytest.raises(IndexError):
        empty_pqueue.pop()
