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
    trie.insert("hi you")
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
    assert list(start.keys()) == ["h"]
    assert list(start["h"].children["e"].children.keys()) == ["y"]


def test_insert_many_words_still_works(multi_trie):
    """Test that when you insert multiple words, the trie still works."""
    assert multi_trie.root.value is None
    assert "o" in multi_trie.root.children["h"].children.keys()
    assert "e" in multi_trie.root.children["h"].children.keys()
    assert "y" and "a" and "l" in multi_trie.root.children["h"].children["e"].children.keys()


def test_check_value_with_short_word(full_trie):
    """Test that insertion tracks word progression correctly."""
    assert full_trie.root.children['h'].children['e'].children['y'].value == "y"


def test_check_value_of_last_letterwith_multi_words(multi_trie):
    """Test that insertion tracks word progression when many words in trie."""
    assert multi_trie.root.children['h'].children['e'].children['l'].children['l'].children['o'].value == 'o'


def test_value_with_spaces_in_word(multi_trie):
    """Test that a space does not break the trie."""
    assert multi_trie.root.children['h'].children['i'].children[' '].value == ' '

# *******************Size Tests***********************************************


def test_insert_string_increases_size(empty_trie):
    """Test that insertion increases size with each node inserted."""
    empty_trie.insert("hey")
    assert empty_trie.size() == 1
    empty_trie.insert("howdy")
    assert empty_trie.size() == 2


def test_insert_a_word_twice_does_not_change_size(empty_trie):
    """Test inserting a word twice does not xhange the size of the trie."""
    empty_trie.insert("hey")
    assert empty_trie.size() == 1
    empty_trie.insert("hey")
    assert empty_trie.size() == 1


def test_size_of_multi_trie(multi_trie):
    """Test that the size of a trie reflects multiple words."""
    assert multi_trie.size() == 6


def test_size_doesnt_change_when_you_run_contains(full_trie):
    """Test that the size attribute is unchanged when you run contains."""
    full_trie.contains("hey")
    assert full_trie.size() == 1


def test_size_changes_on_remove(multi_trie):
    """Test that remove changes the size of the trie."""
    multi_trie.remove("hello")
    assert multi_trie.size() == 5


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


def test_contains_returns_true_for_words_with_spaces(multi_trie):
    """Test that contains returns true if the words have a space."""
    assert multi_trie.contains("hi you") is True


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
    assert multi_trie.contains("hello") is False


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
    assert multi_trie.contains("howdy") is False


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


def test_remove_word_that_branches_from_root_by_itself(empty_trie):
    """Test that removing word that is the only word from that letter."""
    empty_trie.insert("tool")
    empty_trie.remove("tool")
    assert empty_trie.contains("tool") is False

# *******************Traversal Tests*******************************************


def test_traverse_on_empty_trie(empty_trie):
    """Test that traversal on an empty trie returns nothing."""
    assert list(empty_trie.traversal()) == []


def test_traverse_string_on_empty_trie(empty_trie):
    """Test that traversal on an empty trie returns nothing."""
    assert list(empty_trie.traversal('hello')) == []


def test_traversal_with_no_input_string_returns_trie(full_trie):
    """Test that traversal returns the whole trie when input is none or ' '."""
    assert list(full_trie.traversal()) == ['h', 'e', 'y']
    assert list(full_trie.traversal('')) == ['h', 'e', 'y']


def test_input_and_traversal_with_no_input_string_returns_trie(full_trie):
    """Test that traversal returns the whole trie when input is none or ' '."""
    full_trie.insert('hi')
    assert list(full_trie.traversal()) == ['h', 'e', 'y', 'i']
    assert list(full_trie.traversal('')) == ['h', 'e', 'y', 'i']


def test_traversal_with_partial_word_returns_rest_of_word(full_trie):
    """Test that inputing part of a word returns the remaining letters."""
    assert list(full_trie.traversal('h')) == ['e', 'y']


def test_traversal_with_string_not_in_trie(full_trie):
    """Test that traversal returns nothing when input not in trie."""
    assert list(full_trie.traversal("goodbye")) == []


def test_traversal_on_word_with_no_following_letters(full_trie):
    """Test that traversal returns nothing when input == trie."""
    assert list(full_trie.traversal("hey")) == []


def test_traversal_on_input_word_with_no_following_letters(full_trie):
    """Test that traversal returns nothing when inserted input == trie."""
    full_trie.insert("yo")
    assert list(full_trie.traversal("yo")) == []


def test_traversal_on_multi_word_trie_returns_whole_branch(multi_trie):
    """Test that traversal on multitrie returns remaining branch chars."""
    assert list(multi_trie.traversal("he")) == ['y', 'l', 'l', 'o', 'a', 'd']


def test_traversal_on_word_with_space_returns_spaces_too(multi_trie):
    """Test that traversal on a word with a space returns the space."""
    assert list(multi_trie.traversal("hi")) == [' ', 'y', 'o', 'u']


def test_remove_doesnt_break_traversal(multi_trie):
    """Test that removing a shared string does not break traversal."""
    multi_trie.remove('hello')
    assert list(multi_trie.traversal("he")) == ['y', 'l', 'l', 'a', 'd']


def test_traversal_with_non_ascii_chars(full_trie):
    """Test that non ascii characters do not break the traversal."""
    assert list(full_trie.traversal('@#$#^&#')) == []