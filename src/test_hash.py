"""Tests for hash function."""

import pytest
from hash import Hash


@pytest.fixture
def test_hash():
    """An empty binary search tree fixture."""
    hash_table = Hash(10)
    return hash_table


@pytest.fixture
def test_hash_fnv():
    """An empty binary search tree fixture."""
    hash_table = Hash(10, 'fnv')
    return hash_table


def test_that_hash_table_has_the_size_given(test_hash):
    """Test that creating a hash gives it a size."""
    assert len(test_hash._hashtable) == 10


def test_additive_hash_table_returns_appropriate_hash_value(test_hash):
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


def test_fnv_hash_table_returns_appropriate_hash_value(test_hash_fnv):
    """Test that the hash function adds value of each char."""
    assert test_hash_fnv._hash("o") == 0
    assert test_hash_fnv._hash("n") == 1
    assert test_hash_fnv._hash("m") == 2
    assert test_hash_fnv._hash("l") == 3
    assert test_hash_fnv._hash("k") == 4
    assert test_hash_fnv._hash("j") == 5
    assert test_hash_fnv._hash("i") == 6
    assert test_hash_fnv._hash("h") == 7
    assert test_hash_fnv._hash("g") == 8
    assert test_hash_fnv._hash("f") == 9


def test_that_setting_a_non_string_throws_type_error(test_hash):
    """Test that you must pass a string to set."""
    with pytest.raises(TypeError):
        test_hash.set(9, 8)


def test_that_setting_places_key_value_tuple_in_proper_bucket(test_hash):
    """Test that key value pair go into the proper bucket."""
    test_hash.set('m', 'data')
    assert test_hash._hashtable[9][0] == ('m', 'data')


def test_that_setting_places_key_value_in_proper_bucket_fnv(test_hash_fnv):
    """Test fnv hash key value pair go into the proper bucket."""
    test_hash_fnv.set('m', 'data')
    assert test_hash_fnv._hashtable[2][0] == ('m', 'data')


def test_that_hashing_to_bucket_with_value_adds_to_list(test_hash):
    """Test that you can add multiple key value pairs to the bucket."""
    test_hash.set('m', 'data')
    test_hash.set('quiche', 'data2')
    assert len(test_hash._hashtable[9]) == 2


def test_that_hashing_to_bucket_with_value_adds_to_list_fmv(test_hash_fnv):
    """Test fnv hash can add multiple key value pairs to the bucket."""
    test_hash_fnv.set('k', 'data')
    test_hash_fnv.set('quiche', 'data2')
    assert len(test_hash_fnv._hashtable[4]) == 2


def test_that_getting_key_returns_proper_value(test_hash):
    """Test that you can get the value by getting key."""
    test_hash.set('m', 'data')
    test_hash.set('quiche', 'data2')
    assert test_hash.get('m') == 'data'
    assert test_hash.get('quiche') == 'data2'


def test_that_getting_key_returns_proper_value_fnv(test_hash_fnv):
    """Test fnv hash can get the value by getting key."""
    test_hash_fnv.set('m', 'data')
    test_hash_fnv.set('quiche', 'data2')
    assert test_hash_fnv.get('m') == 'data'
    assert test_hash_fnv.get('quiche') == 'data2'


def test_that_setting_key_more_than_once_updates_value(test_hash):
    """Test that adding to table with key already in hash replaces value."""
    test_hash.set('m', 'data')
    assert test_hash.get('m') == 'data'
    test_hash.set('m', 'data3')
    assert test_hash.get('m') == 'data3'


def test_that_setting_key_more_than_once_updates_value_fnv(test_hash_fnv):
    """Test fnv hash adding to table with key already in hash replaces value."""
    test_hash_fnv.set('m', 'data')
    assert test_hash_fnv.get('m') == 'data'
    test_hash_fnv.set('m', 'data3')
    assert test_hash_fnv.get('m') == 'data3'
