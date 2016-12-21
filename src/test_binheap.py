"""Test binary heap."""


import pytest


@pytest.fixture
def empty_heap():
    """Fixture for empty heap."""
    from binheap import Binheap
    heap = Binheap()
    return heap


@pytest.fixture
def full_heap():
    """Fixture for full heap."""
    from binheap import Binheap
    heap = Binheap([1, 2, 3])
    return heap


def test_empty_heap_is_empty(empty_heap):
    """Test that empty head has empty list."""
    assert len(empty_heap.heap) == 0


def test_fully_heap_is_full(full_heap):
    """Test that full heap has data."""
    assert len(full_heap.heap) == 3
