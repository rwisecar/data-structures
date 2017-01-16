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


def test_cant_init_w_noniter():
    """Test you can't instantiate heap with noniterable."""
    from binheap import Binheap
    with pytest.raises(TypeError):
        Binheap(8675309)


def test_empty_heap_is_empty(empty_heap):
    """Test that empty head has empty list."""
    assert len(empty_heap.heap) == 0


def test_fully_heap_is_full(full_heap):
    """Test that full heap has data."""
    assert len(full_heap.heap) == 3


def test_instantiate_with_list_sorts(full_heap):
    """Test that index 0 is smallest value."""
    assert full_heap.heap[0] == 1


def test_push_to_empty_heap(empty_heap):
    """Test push adds to empty heap."""
    empty_heap.push(8)
    assert empty_heap.heap == [8]


def test_push_to_populated_heap_works(full_heap):
    """Test pushing to populated heap adds to heap."""
    full_heap.push(8)
    assert len(full_heap.heap) == 4


def test_push_to_populated_heap_sorts(full_heap):
    """Test push sorts as expected."""
    full_heap.push(0)
    assert full_heap.heap[0] == 0


def test_push_to_populated_heap_sorts_bigger_num(full_heap):
    """Test push's sorting with larger number."""
    full_heap.push(5)
    full_heap.push(3)
    assert full_heap.heap[3] == 5


def test_pop_from_empty(empty_heap):
    """Test you can't pop from empty heap."""
    with pytest.raises(IndexError):
        empty_heap.pop()


def test_pop_returns_value(full_heap):
    """Test pop returns proper value."""
    assert full_heap.pop() == 1


def test_pop_sorts_heap_structure(full_heap):
    """Test that pop sorts heap structure."""
    full_heap.pop()
    assert full_heap.heap[0] == 2




