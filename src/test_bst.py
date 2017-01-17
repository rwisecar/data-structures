"""Tests for bst.py Binary Search Tree."""

import pytest
from bst import Node, BST


@pytest.fixture
def test_bst():
    """An empty binary search tree fixture."""
    bst = BST()
    return bst


@pytest.fixture
def filled_bst():
    """A filled bst."""
    bst = BST([10, 15, 5, 3, 20])
    return bst


@pytest.fixture
def traversal_bst():
    """A filled bst."""
    bst = BST([6, 7, 8, 9, 2, 1, 4, 3, 5])
    return bst


@pytest.fixture
def left_leaning_bst(test_bst):
    """A left leaning filled bst."""
    test_bst.insert(10)
    test_bst.insert(9)
    test_bst.insert(8)
    test_bst.insert(7)
    test_bst.insert(6)
    test_bst.insert(5)
    test_bst.insert(4)
    test_bst.insert(3)
    test_bst.insert(2)
    test_bst.insert(1)
    return test_bst


@pytest.fixture
def right_leaning_bst(test_bst):
    """A right leaning filled bst."""
    test_bst.insert(1)
    test_bst.insert(2)
    test_bst.insert(3)
    test_bst.insert(4)
    test_bst.insert(5)
    test_bst.insert(6)
    test_bst.insert(7)
    test_bst.insert(8)
    test_bst.insert(9)
    test_bst.insert(10)
    return test_bst


def test_empty_node_has_no_root():
    """Test that initializing a root has empoty attriubutes."""
    node = Node()
    assert node.value is None
    assert node.left_child is None
    assert node.right_child is None


def test_an_empty_bst_root_is_none():
    """Test that initalizing a bst results in a bst with no root and size 0."""
    bst = BST()
    assert bst.root is None
    assert bst.size() == 0


def test_adding_to_empty_tree_adds_new_root(test_bst):
    """Test that add to an emptyr tree rassigns root to the new node."""
    test_bst.insert(10)
    assert test_bst.root.value == 10
    assert test_bst.size() == 1


def test_adding_value_greater_than_root_value_adds_right_child(test_bst):
    """Test that adding a value greater than the root value adds to the right child."""
    test_bst.insert(10)
    test_bst.insert(15)
    assert test_bst.root.right_child.value == 15
    assert test_bst.root.left_child is None


def test_adding_value_less_than_root_value_adds_left_child(test_bst):
    """Test that adding a value less than the root value adds to the leftchild."""
    test_bst.insert(10)
    test_bst.insert(5)
    assert test_bst.root.left_child.value == 5
    assert test_bst.root.right_child is None


def test_adding_value_equal_to_root_value_adds_nothing(test_bst):
    """Test that adding a value greater than the root value adds to the right child."""
    test_bst.insert(10)
    test_bst.insert(10)
    assert test_bst.root.right_child is None
    assert test_bst.root.left_child is None


def test_adding_values_adds_to_the_size_of_the_bst(test_bst):
    """Test that inserting adds to the size of the tree."""
    assert test_bst.size() == 0
    test_bst.insert(10)
    assert test_bst.size() == 1
    test_bst.insert(15)
    assert test_bst.size() == 2
    test_bst.insert(10)
    assert test_bst.size() == 2


def test_iterable_creates_proper_bst():
    """Test using an iterable properly fills the tree."""
    bst = BST([10, 15, 5, 3, 20])
    assert bst.root.value == 10
    assert bst.root.left_child.value == 5
    assert bst.root.left_child.left_child.value == 3
    assert bst.root.right_child.value == 15
    assert bst.root.right_child.right_child.value == 20
    assert bst.size() == 5


def test_create_bst_with_non_iterable_raises_type_error():
    """Test that initializing with a non iterable raises typeerror."""
    with pytest.raises(TypeError):
        BST(9)


def test_search_for_root_value_returns_root(filled_bst):
    """Test that serching for root value returns the root node."""
    assert filled_bst.search(10) == filled_bst.root


def test_search_for_roots_left_child_value_returns_left_child(filled_bst):
    """Test that search returns the proper node."""
    assert filled_bst.search(5) == filled_bst.root.left_child


def test_search_for_roots_right_child_value_returns_right_child(filled_bst):
    """Test that search returns the proper node."""
    assert filled_bst.search(15) == filled_bst.root.right_child


def test_search_for_large_value_not_in_tree_returns_none(filled_bst):
    """Search for value not in tree returns none."""
    assert filled_bst.search(100) is None


def test_search_for_small_value_not_in_tree_returns_none(filled_bst):
    """Search for value not in tree returns none."""
    assert filled_bst.search(1) is None


def test_depth_on_empty_tree_is_zero(test_bst):
    """Depth of empty tree is zero."""
    assert test_bst.depth() == 0


def test_depth_0n_filled_bst_returns_proper_depth(filled_bst):
    """Test that a tree that is 3 deep returns a depth of three."""
    assert filled_bst.depth() == 3


def test_depth_on_left_leaning_tree_returns_proper_depth(left_leaning_bst):
    """Test that depth search on a left leaning bst with ten values returns a depth of 10."""
    assert left_leaning_bst.depth() == 10


def test_depth_on_right_leaning_tree_returns_proper_depth(right_leaning_bst):
    """Test that depth search on a left leaning bst with ten values returns a depth of 10."""
    assert right_leaning_bst.depth() == 10


def test_contains_on_root_value_returns_true(filled_bst):
    """Test that contains for root value returns true."""
    assert filled_bst.contains(10) is True


def test_contains_on_roots_left_child_value_returns_true(filled_bst):
    """Test that contains returns the proper boolean."""
    assert filled_bst.contains(5) is True


def test_contains_on_roots_right_child_value_returns_true(filled_bst):
    """Test that contains returns the proper boolean."""
    assert filled_bst.contains(5) is True


def test_contains_on_large_value_not_in_tree_returns_false(filled_bst):
    """Search for value not in tree returns false."""
    assert filled_bst.contains(100) is False


def test_contains_on_small_value_not_in_tree_returns_false(filled_bst):
    """Search for value not in tree returns false."""
    assert filled_bst.contains(1) is False


def test_balanced_on_empty_tree_returns_zero(test_bst):
    """Balance of a empty tree is zero."""
    assert test_bst.balance() == 0


def test_balanced_works_on_filled_bst(filled_bst):
    """Check for balance of the filled bst is true."""
    assert filled_bst.balance() == 0


def test_balance_on_left_leaning_tree_returns_proper_depth(left_leaning_bst):
    """Test that balance search on a left leaning bst with ten values returns a balance of -9."""
    assert left_leaning_bst.balance() == -9


def test_balance_on_right_leaning_tree_returns_proper_depth(right_leaning_bst):
    """Test that balance search on a right leaning bst with ten values returns a balance of 9."""
    assert right_leaning_bst.balance() == 9


def test_the_balance_of_a_tree_as_its_built(test_bst):
    """Build a tree and verify its balance as its built."""
    test_bst.insert(5)
    assert test_bst.balance() == 0
    test_bst.insert(1)
    assert test_bst.balance() == -1
    test_bst.insert(0)
    assert test_bst.balance() == -2
    test_bst.insert(9)
    assert test_bst.balance() == -1
    test_bst.insert(8)
    assert test_bst.balance() == 0


# ********************* TRAVERSAL TESTING ************************************
def test_that_in_order_traversal_of_empty_tree_returns_empty(test_bst):
    """Test that traversal on an empty tree returns empty results."""
    assert test_bst.in_order_traversal() == []


def test_that_in_order_traversal_produces_correct_results(traversal_bst):
    """Test that ttraversal on basic tree works."""
    assert traversal_bst.in_order_traversal() == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_that_pre_order_traversal_of_empty_tree_returns_empty(test_bst):
    """Test that traversal on an empty tree returns empty results."""
    assert test_bst.pre_order_traversal() == []


def test_that_pre_order_traversal_produces_correct_results(traversal_bst):
    """Test that ttraversal on basic tree works."""
    assert traversal_bst.pre_order_traversal() == [6, 2, 1, 4, 3, 5, 7, 8, 9]


def test_that_post_order_traversal_of_empty_tree_returns_empty(test_bst):
    """Test that traversal on an empty tree returns empty results."""
    assert test_bst.post_order_traversal() == []


def test_that_post_order_traversal_produces_correct_results(traversal_bst):
    """Test that ttraversal on basic tree works."""
    assert traversal_bst.post_order_traversal() == [1, 3, 5, 4, 2, 9, 8, 7, 6]


def test_that_breadth_first_traversal_of_empty_tree_returns_empty(test_bst):
    """Test that traversal on an empty tree returns empty results."""
    assert test_bst.breadth_first_traversal() == []


def test_that_breadth_first_traversal_produces_correct_results(traversal_bst):
    """Test that ttraversal on basic tree works."""
    assert traversal_bst.breadth_first_traversal() == [6, 2, 7, 1, 4, 8, 3, 5, 9]
