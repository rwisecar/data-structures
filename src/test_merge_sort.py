"""Test merge_sort.py."""

from merge_sort import merge_sort
import pytest


def test_merge_sort_works_on_an_iterable_of_numbers():
    """Test that you can merge_sort a list of numbers."""
    assert merge_sort([4, 6, 2, 3, 1, 5]) == [1, 2, 3, 4, 5, 6]


def test_merge_sort_works_on_an_iterable_of__negative_numbers():
    """Test that you can merge_sort a list containing negative numbers."""
    assert merge_sort([-4, -6, -2, 3, 1, 5]) == [-6, -4, -2, 1, 3, 5]


def test_merge_sort_works_on_an_iterable_of_char():
    """Test that you can merge_sort a list of char."""
    assert merge_sort(['f', 'd', 'a', 'c', 'e', 'b']) == ['a', 'b', 'c', 'd', 'e', 'f']


def test_merge_sort_works_on_an_iterable_of_strings():
    """Test that you can merge_sort a list of char."""
    assert merge_sort(['boom', 'doom', 'room', 'because', 'jokes', 'rule']) == ['because', 'boom', 'doom', 'jokes', 'room', 'rule']


def test_merge_sort_fails_on_strings():
    """Test that you can merge_sort a list of char."""
    with pytest.raises(TypeError):
        merge_sort('dags')


def test_merge_sort_on_dict_raises_error():
    """Test that you must have an iterable to sort."""
    with pytest.raises(TypeError):
        merge_sort({'a': 1, 'b': 2})


def test_merge_sort_on_non_iterable_raises_error():
    """Test that you must have an iterable to sort."""
    with pytest.raises(TypeError):
        merge_sort(8)


def test_merge_sort_on_very_large_list():
    import random
    vll = [random.randint(0, 10000) for x in range(1, 100)]
    assert merge_sort(vll) == sorted(vll)
