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

ADDITIVE_TEST_TABLE = [
    ['d', 0],
    ['e', 1],
    ['f', 2],
    ['g', 3],
    ['h', 4],
    ['i', 5],
    ['j', 6],
    ['k', 7],
    ['l', 8],
    ['m', 9],
]

FNV_TEST_TABLE = [
    ['f', 0],
    ['g', 9],
    ['h', 8],
    ['i', 7],
    ['j', 6],
    ['k', 5],
    ['l', 4],
    ['m', 3],
    ['n', 2],
    ['o', 1],
]


def test_that_hash_table_has_the_size_given(test_hash):
    """Test that creating a hash gives it a size."""
    assert len(test_hash._hashtable) == 10


@pytest.mark.parametrize("char, result", ADDITIVE_TEST_TABLE)
def test_additive_hash_table_returns_appropriate_hash_value(char, result, test_hash):
    """Test that the hash function adds value of each char."""
    assert test_hash._hash(char) == result


@pytest.mark.parametrize("char, result", FNV_TEST_TABLE)
def test_fnv_hash_table_returns_appropriate_hash_value(char, result, test_hash_fnv):
    """Test that the hash function adds value of each char."""
    assert test_hash_fnv._hash(char) == result


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
    assert test_hash_fnv._hashtable[3][0] == ('m', 'data')


def test_that_hashing_to_bucket_with_value_adds_to_list(test_hash):
    """Test that you can add multiple key value pairs to the bucket."""
    test_hash.set('m', 'data')
    test_hash.set('quiche', 'data2')
    assert len(test_hash._hashtable[9]) == 2


def test_that_hashing_to_bucket_with_value_adds_to_list_fmv(test_hash_fnv):
    """Test fnv hash can add multiple key value pairs to the bucket."""
    test_hash_fnv.set('k', 'data')
    test_hash_fnv.set('u', 'data2')
    assert len(test_hash_fnv._hashtable[5]) == 2


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
