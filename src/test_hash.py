"""Tests for hash function."""

import pytest
from hash import Hash


@pytest.fixture
def test_hash():
    """An empty binary search tree fixture."""
    hash_table = Hash(10)
    return hash_table


def test_that_hash_table_has_the_size_given(test_hash):
    """Test that creating a hash gives it a size."""
    assert len(test_hash._hashtable) == 10


def test_hash_table_returns_appropriate_hash_value(test_hash):
    """Test that the hash function adds value of each char."""
    assert test_hash._hash("d") == 0
    assert test_hash._hash("e") == 1
    assert test_hash._hash("f") == 2
    assert test_hash._hash("g") == 3
    assert test_hash._hash("h") == 4
    assert test_hash._hash("i") == 5
    assert test_hash._hash("j") == 6
    assert test_hash._hash("k") == 7
    assert test_hash._hash("l") == 8
    assert test_hash._hash("m") == 9


def test_that_seting_a_non_string_throws_type_error(test_hash):
    """Test that you must pass a string to set."""
    with pytest.raises(TypeError):
        test_hash.set(9, 8)


def test_that_setting_places_key_value_tuple_in_proper_bucket(test_hash):
    """Test that key value pair go into the proper bucket."""
    test_hash.set('m', 'data')
    assert test_hash._hashtable[9][0] == ('m', 'data')


def test_that_hashing_to_bucket_with_value_adds_to_list(test_hash):
    """Test that you can add multiple key value pairs to the bucket."""
    test_hash.set('m', 'data')
    test_hash.set('quiche', 'data2')
    assert len(test_hash._hashtable[9]) == 2


def test_that_getting_key_returns_proper_value(test_hash):
    """Test that you can get the value by getting key."""
    test_hash.set('m', 'data')
    test_hash.set('quiche', 'data2')
    assert test_hash.get('m') == 'data'
    assert test_hash.get('quiche') == 'data2'
