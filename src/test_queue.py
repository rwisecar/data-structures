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
