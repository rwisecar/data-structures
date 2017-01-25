"""Test functionality of Trie implementation."""

import pytest
from trie import Trie, TrieNode


@pytest.fixture
def empty_trie():
    """Create an empty trie."""
    trie = Trie()
    return trie


@pytest.fixture
def full_trie():
    """Create a full trie."""
    trie = Trie()
    trie.insert("hey")
    return trie


@pytest.fixture
def multi_trie():
    """Create a tree with multiple words."""
    trie = Trie()
    trie.insert("hey")
    trie.insert("hell")
    trie.insert("hello")
    trie.insert("howdy")
    trie.insert("head")
    return trie


def test_create_empty_trie(empty_trie):
    """Test that you can create an empty trie."""
    assert empty_trie.root.children == {}
    assert empty_trie._size == 0


def test_create_trienode():
    """Test that you can create a trienode with a specific value."""
    node = TrieNode("h")
    assert node.value == "h"
    assert node.children == {}


# *******************Insert Tests********************************************


def test_insert_non_string_raises_type_error(empty_trie):
    """Test that inserting a non string raises a TypeError."""
    with pytest.raises(TypeError):
        empty_trie.insert(569)


def test_insert_string_has_correct_key_value_pairs(empty_trie):
    """Test that you can insert a string, node by node."""
    empty_trie.insert("hey")
    start = empty_trie.root.children
    assert empty_trie.root.value is None
    assert start.keys() == ["h"]
    assert start["h"].children["e"].children.keys() == ["y"]


def test_insert_many_words_still_works(multi_trie):
    """Test that when you insert multiple words, the trie still works."""
    assert multi_trie.root.value is None
    assert "o" in multi_trie.root.children["h"].children.keys()
    assert "e" in multi_trie.root.children["h"].children.keys()
    assert "y" and "a" and "l" in multi_trie.root.children["h"].children["e"].children.keys()


def test_insert_string_tracks_word_progression(full_trie):
    """Test that insertion tracks word progression correctly."""
    assert full_trie.root.children['h'].children['e'].children['y'].value == "hey"


def test_track_word_progression_with_multi_words(multi_trie):
    """Test that insertion tracks word progression when many words in trie."""
    assert multi_trie.root.children['h'].children['e'].children['l'].children['l'].children['o'].value == 'hello'


# *******************Size Tests***********************************************


def test_insert_string_increases_size(empty_trie):
    """Test that insertion increases size with each node inserted."""
    empty_trie.insert("hey")
    assert empty_trie._size == 1
    empty_trie.insert("howdy")
    assert empty_trie._size == 2


def test_size_of_multi_trie(multi_trie):
    """Test that the size of a trie reflects multiple words."""
    assert multi_trie._size == 5


def test_size_doesnt_change_when_you_run_contains(full_trie):
    """Test that the size attribute is unchanged when you run contains."""
    full_trie.contains("hey")
    assert full_trie._size == 1


def test_size_changes_on_remove(multi_trie):
    """Test that remove changes the size of the trie."""
    multi_trie.remove("hello")
    assert multi_trie._size == 4


# *******************Contains Tests********************************************


def test_contains_returns_false_when_word_not_in_trie(empty_trie, full_trie):
    """Test that contains returns false when string not in trie."""
    assert empty_trie.contains("goodbye") is False
    assert full_trie.contains("goodbye") is False


def test_contains_returns_false_when_word_mismatches(full_trie):
    """Test that contains returns false when match is not perfect."""
    assert full_trie.contains("hello") is False


def test_contains_raises_key_error_when_partial_word_searched(full_trie):
    """Test that a KeyError is raised when you search for part of a word."""
    with pytest.raises(KeyError):
        full_trie.contains("he")


def test_contains_raises_type_error_when_non_string_searched(full_trie):
    """Test that contains returns false when you search for a nonstring."""
    with pytest.raises(TypeError):
        full_trie.contains(569)


def test_contains_returns_true_when_word_in_trie(full_trie):
    """Test that contains returns true when string in trie."""
    assert full_trie.contains("hey") is True


def test_contains_returns_true_for_partial_word_in_multi_word_trie(multi_trie):
    """Test that contains returns true for shorter word in multi_trie."""
    assert multi_trie.contains("hell") is True


# *******************Removes Tests********************************************


def test_remove_word_raises_key_error_when_word_not_in_trie(full_trie):
    """Test that a KeyError is raised when you remove a word not in trie."""
    with pytest.raises(KeyError):
        full_trie.remove("tool")


def test_remove_word_from_empty_trie(empty_trie):
    with pytest.raises(KeyError):
        empty_trie.remove("tool")


def test_remove_non_string_raises_type_error(full_trie):
    """Test that if you try to remove a non string, a TypeError is raised."""
    with pytest.raises(TypeError):
        full_trie.remove(103)


def test_remove_longer_word_removes_word(multi_trie):
    """Test that you can remove a word and that word won't be in the trie."""
    multi_trie.remove("hello")
    with pytest.raises(KeyError):
        multi_trie.contains("hello")


def test_remove_longer_word_retains_all_shorter_words(multi_trie):
    """Test that when you remove a word, the other words remain intact."""
    multi_trie.remove("hello")
    assert multi_trie.contains("hey") is True
    assert multi_trie.contains("hell") is True
    assert multi_trie.contains("head") is True
    assert multi_trie.contains("howdy") is True


def test_remove_word_with_one_bifurcation(multi_trie):
    """Test that you can remove a word with only one bifurcation."""
    multi_trie.remove("howdy")
    with pytest.raises(KeyError):
        multi_trie.contains("howdy")


def test_remove_one_bifurcation_word_retains_all_other_words(multi_trie):
    """Test that removing word with one bifurcation retains all other words."""
    multi_trie.remove("howdy")
    assert multi_trie.contains("hey") is True
    assert multi_trie.contains("hell") is True
    assert multi_trie.contains("head") is True
    assert multi_trie.contains("hello") is True


def test_remove_shorter_word_retains_longer_form_of_that_word(multi_trie):
    """Test that removing word that is part of a bigger word keeps big word."""
    multi_trie.remove("hell")
    assert multi_trie.contains("hello") is True
