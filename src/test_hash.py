"""Tests for hash function."""

import pytest
from hash import Hash


def test_that_hash_table_has_the_size_given():
    """Test that creating a hash gives it a size."""
    hash_table = Hash(1024)
    assert len(hash_table._hashtable) == 1024
