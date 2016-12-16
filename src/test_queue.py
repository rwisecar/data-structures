"""Test for queue.py modeule."""

import pytest


@pytest.fixture
def new_queue():
    """Create  new Queue."""
    from queue import Queue
    this_queue = Queue()
    return this_queue


@pytest.fixture
def value_queue():
    """Create a Queue with value."""
    from queue import Queue
    this_full_queue = Queue(iterable=[1, 2, 3])
    return this_full_queue


def test_new_queue_empty(new_queue):
    """Cheecking for empty Queue to ensure its empty."""
    assert new_queue._queue._length == 0


def test_full_queue(value_queue):
    """Checking for something in the Queue."""
    assert value_queue._queue._length == 3


def test_enqueue_adds_value(value_queue):
    """Checking for the value tranported to the tail."""
    value_queue.enqueue(15)
    assert value_queue._queue.tail.value == 15


def test_enqueue_empty_queue(new_queue):
    """Checking adding an item into an empty queue list."""
    new_queue.enqueue(15)
    assert new_queue._queue.tail.value == 15


def test_equeue_queue_length(value_queue):
    """Checking for the length of queue."""
    value_queue.enqueue(15)
    assert value_queue._queue._length == 4


def test_dequeue_with_value(value_queue):
    """Test that you can remove head of queue."""
    value_queue.dequeue()
    assert value_queue._queue.head.value == 2


def test_dequeue_with_empty_list(new_queue):
    """Check index error when you call dequeue on empty queue."""
    with pytest.raises(IndexError):
        new_queue.dequeue()


def test_length_of_queue_when_dequeued(value_queue):
    """Check length of queue when you call dequeue."""
    value_queue.dequeue()
    assert value_queue._queue._length == 2


def test_length_of_empty_queue(new_queue):
    """Check that length of empty queue returns 0."""
    assert new_queue.size() == 0


def test_length_of_full_queue(value_queue):
    """Check that length of full queue returns length of queue."""
    assert value_queue.size() == 3


def test_peek_returns_value(value_queue):
    """Check that peek returns the value of the next node."""
    assert value_queue.peek(2) == 1


def test_peek_returns_none_if_empty_queue(new_queue):
    """Check that peek returns None if queue is empty."""
    assert new_queue.peek(15) is None


def test_peek_head_of_queue(value_queue):
    """Check that peek works with head of queue."""
    assert value_queue.peek(3) == 2


def test_peek_tail_of_queue(value_queue):
    """Check that peek works with tail of queue."""
    assert value_queue.peek(1) is None
