"""Tests for the quicksort sort."""

from quicksort import quicksort
import pytest


def test_quicksort_works_on_an_iterable_of_numbers():
    """Test that you can quicksort a list of numbers."""
    assert quicksort([4, 6, 2, 3, 1, 5]) == [1, 2, 3, 4, 5, 6]


def test_quicksort_works_on_an_iterable_of__negative_numbers():
    """Test that you can quicksort a list containing negative numbers."""
    assert quicksort([-4, -6, -2, 3, 1, 5]) == [-6, -4, -2, 1, 3, 5]


def test_quicksort_works_on_an_iterable_of_char():
    """Test that you can quicksort a list of char."""
    assert quicksort(['f', 'd', 'a', 'c', 'e', 'b']) == ['a', 'b', 'c', 'd', 'e', 'f']


def test_quicksort_works_on_an_iterable_of_strings():
    """Test that you can quicksort a list of char."""
    assert quicksort(['boom', 'doom', 'room', 'because', 'jokes', 'rule']) == ['because', 'boom', 'doom', 'jokes', 'room', 'rule']


def test_quicksort_fails_on_strings():
    """Test that you can quicksort a list of char."""
    with pytest.raises(TypeError):
        quicksort('dags')


def test_quicksort_on_dict_raises_error():
    """Test that you must have an iterable to sort."""
    with pytest.raises(TypeError):
        quicksort({'a': 1, 'b': 2})


def test_quicksort_on_non_iterable_raises_error():
    """Test that you must have an iterable to sort."""
    with pytest.raises(TypeError):
        quicksort(8)
