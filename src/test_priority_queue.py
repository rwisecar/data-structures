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


def test_insert_negative_priority(populated_pqueue):
    """Test that a negative priority can be added to a populated queue."""
    populated_pqueue.insert(5, -1)
    assert populated_pqueue._priorityq[3] == (5, -1)


def test_insert_adds_to_q(empty_pqueue):
    """Test that inserted value is add."""
    empty_pqueue.insert('Bellingham', 2)
    assert empty_pqueue._priorityq[0] == ('Bellingham', 2)


def test_cant_pop_from_empty(empty_pqueue):
    """Test that pop raises error on empty queue."""
    with pytest.raises(IndexError):
        empty_pqueue.pop()


def test_pop_from_full(populated_pqueue):
    """Test that pop is functional from populated queue."""
    populated_pqueue.pop()
    assert len(populated_pqueue._priorityq) == 2


def test_pop_from_full_removes_high_priority_tuple(populated_pqueue):
    """Test that pop removes the tuple with the highest priority."""
    populated_pqueue.pop()
    assert ('Seattle', 1) not in populated_pqueue._priorityq


def test_pop_two_items_same_priority(populated_pqueue):
    """Test that pop removes only first instance of a duplicated high priority."""
    populated_pqueue.insert('New York', 1)
    populated_pqueue.pop()
    assert ('Seattle', 1) not in populated_pqueue._priorityq
    assert ('New York', 1) in populated_pqueue._priorityq


def test_pop_negative_priority(empty_pqueue):
    """Test that pop() sorts, removes negative number."""
    empty_pqueue.insert(5, 0)
    empty_pqueue.insert(10, -1)
    empty_pqueue.pop()
    assert empty_pqueue._priorityq[0][0] == 5


def test_peek_from_empty(empty_pqueue):
    """Test can't peek at empty."""
    with pytest.raises(IndexError):
        empty_pqueue.peek()


def test_peek_from_populated_q(populated_pqueue):
    """Test peek works as exoected on prepoulated queue."""
    assert populated_pqueue.peek() == ('Seattle', 1)


def test_peek_w_two_at_same_prio(populated_pqueue):
    """Test peek returns first of multiple same prio."""
    populated_pqueue.insert('New York', 1)
    assert populated_pqueue.peek() == ('Seattle', 1)


def test_peek_returns_lowest_neg_prio(empty_pqueue):
    """Test that peek sorts, returns lowest negative number."""
    empty_pqueue.insert(5, 0)
    empty_pqueue.insert(10, -1)
    empty_pqueue.insert(8, -3)
    assert empty_pqueue.peek() == (8, -3)
