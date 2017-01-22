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


@pytest.fixture
def simple_left_unbalanced():
    bst = BST([3, 2, 1])
    return bst


@pytest.fixture
def simple_right_unbalanced():
    bst = BST([1, 2, 3])
    return bst


@ pytest.fixture
def complex_left_unbalanced():
    bst = BST([10, 15, 7, 5, 8, 6])
    return bst


@pytest.fixture
def complex_right_unbalanced():
    bst = BST([10, 20, 30, 25])
    return bst


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


def test_depth_on_empty_tree_is_negative(test_bst):
    """Depth of empty tree is zero."""
    assert test_bst.depth() == -1


def test_depth_0n_filled_bst_returns_proper_depth(filled_bst):
    """Test that a tree that is 3 deep returns a depth of three."""
    assert filled_bst.depth() == 2


def test_depth_on_left_leaning_tree_returns_proper_depth(left_leaning_bst):
    """Test that depth search on a left leaning bst with ten values returns a depth of 10."""
    assert left_leaning_bst.depth() == 3


def test_depth_on_right_leaning_tree_returns_proper_depth(right_leaning_bst):
    """Test that depth search on a left leaning bst with ten values returns a depth of 10."""
    assert right_leaning_bst.depth() == 3


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
    assert left_leaning_bst.balance() == -1


def test_balance_on_right_leaning_tree_returns_proper_depth(right_leaning_bst):
    """Test that balance search on a right leaning bst with ten values returns a balance of 9."""
    assert right_leaning_bst.balance() == 1


def test_the_balance_of_a_tree_as_its_built(test_bst):
    """Build a tree and verify its balance as its built."""
    test_bst.insert(5)
    assert test_bst.balance() == 0
    test_bst.insert(2)
    assert test_bst.balance() == -1
    test_bst.insert(1)
    assert test_bst.balance() == 0
    test_bst.insert(9)
    assert test_bst.balance() == 1
    test_bst.insert(8)
    assert test_bst.balance() == 0


# ********************* TRAVERSAL TESTING ************************************
def test_that_in_order_traversal_of_empty_tree_returns_empty(test_bst):
    """Test that traversal on an empty tree returns empty results."""
    assert test_bst.in_order_traversal() == []


def test_that_in_order_traversal_produces_correct_results(traversal_bst):
    """Test that traversal on basic tree works."""
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

# ********************* DELETE TESTING ************************************


def test_delete_from_empty_bst_is_none(test_bst):
    """Test that delete from empty bst returns none and nothing changed."""
    assert test_bst.delete(1) is None
    assert test_bst.root is None


def test_delete_root_with_no_left_child_moves_right_child_to_root(test_bst):
    """Test that deleting root with only a right child moves that child to root."""
    test_bst.insert(5)
    test_bst.insert(10)
    test_bst.delete(5)
    assert test_bst.root.value == 10


def test_delete_root_with_no_right_child_moves_left_child_to_root(test_bst):
    """Test that deleting root with only a left child moves that child to root."""
    test_bst.insert(10)
    test_bst.insert(5)
    test_bst.delete(10)
    assert test_bst.root.value == 5


def test_remove_root_from_bst_depth_greater_than_two(traversal_bst):
    """Test remove root from a bst with a depth greater than two functions."""
    assert traversal_bst.delete(6) is None
    assert traversal_bst.root.value == 7
    assert traversal_bst.root.left_child.value == 2
    assert traversal_bst.root.right_child.value == 8


def test_remove_leaf_of_bst_depth_greater_than_two(traversal_bst):
    """Test that removing a leaf from a bst with a depth greater than two works."""
    assert traversal_bst.delete(3) is None
    assert traversal_bst.contains(3) is False


def test_remove_node_of_bst_in_middle_of_graph_with_left_child(traversal_bst):
    """Test that removing a node from the middle of a bst with a left child successor."""
    assert traversal_bst.delete(2) is None
    assert traversal_bst.contains(2) is False
    assert traversal_bst.root.left_child.value == 3


def test_remove_node_of_bst_in_middle_of_graph_with_right_child(traversal_bst):
    """Test that removing a node from the middle of a bst with a left child successor."""
    assert traversal_bst.size() == 9
    assert traversal_bst.delete(4) is None
    assert traversal_bst.size() == 8
    assert traversal_bst.contains(4) is False
    assert traversal_bst.root.left_child.right_child.value == 5


def test_remove_value_not_in_bst_leaves_bst_untouched(test_bst):
    """Test that trying to remove a val not in tree does nothing."""
    test_bst.insert(5)
    test_bst.insert(4)
    test_bst.insert(6)
    assert test_bst.size() == 3
    test_bst.delete(10)
    assert test_bst.size() == 3
    assert test_bst.contains(5) is True
    assert test_bst.contains(4) is True
    assert test_bst.contains(6) is True
    assert test_bst.contains(10) is False


# ********************* SELF-BALANCE TESTING **********************************


def test_single_rotation_balance_on_left_heavy_tree(simple_left_unbalanced):
    """Test that a simple left heavy tree self balances with left rotation."""
    assert simple_left_unbalanced.breadth_first_traversal() == [2, 1, 3]


def test_balance_on_insertion_to_simple_left_tree(simple_left_unbalanced):
    """Test that a simple left heavy tree self balances with left rotation."""
    simple_left_unbalanced.insert(2.5)
    simple_left_unbalanced.insert(2.8)
    assert simple_left_unbalanced.breadth_first_traversal() == [
        2.5, 2, 3, 1, 2.8]


def test_deletion_to_simple_left_tree(simple_left_unbalanced):
    """Test that deletion from tree retains bst integrity."""
    simple_left_unbalanced.delete(2)
    assert simple_left_unbalanced.breadth_first_traversal() == [3, 1]


def test_deletion_after_insertion_to_simple_left_tree(simple_left_unbalanced):
    """Test that deletion still works after insertion to tree."""
    simple_left_unbalanced.insert(2.5)
    simple_left_unbalanced.insert(2.8)
    simple_left_unbalanced.delete(2)
    assert simple_left_unbalanced.breadth_first_traversal() == [2.5, 1, 3, 2.8]


def test_insert_zero_to_simple_left_tree(simple_left_unbalanced):
    """Test that insertion still works with 0."""
    simple_left_unbalanced.insert(0)
    assert simple_left_unbalanced.breadth_first_traversal() == [2, 1, 3, 0]


def test_single_rotation_balance_on_right_heavy_tree(simple_right_unbalanced):
    """Test that a simple right heavy tree self balances with left rotation."""
    assert simple_right_unbalanced.breadth_first_traversal() == [2, 1, 3]


def test_balance_on_insertion_to_simple_right_tree(simple_right_unbalanced):
    """Test that a simple left heavy tree self balances with left rotation."""
    simple_right_unbalanced.insert(4)
    simple_right_unbalanced.insert(5)
    assert simple_right_unbalanced.breadth_first_traversal() == [3, 2, 4, 1, 5]


def test_deletion_to_simple_right_tree(simple_right_unbalanced):
    """Test that deletion from tree retains bst integrity."""
    simple_right_unbalanced.delete(3)
    assert simple_right_unbalanced.breadth_first_traversal() == [2, 1]


def test_deletion_post_insertion_to_simple_right_tree(simple_right_unbalanced):
    """Test that deletion still works after insertion to tree."""
    simple_right_unbalanced.insert(4)
    simple_right_unbalanced.insert(5)
    simple_right_unbalanced.delete(3)
    assert simple_right_unbalanced.breadth_first_traversal() == [4, 2, 5, 1]


def test_self_balancing_on_right_heavy_tree(complex_right_unbalanced):
    """Test that the tree self balances as you insert nodes."""
    assert complex_right_unbalanced.breadth_first_traversal() == [
        20, 10, 30, 25]


def test_adding_to_right_heavy_tree_self_balances(complex_right_unbalanced):
    """Test that the tree self balances when you add a new node."""
    complex_right_unbalanced.insert(23)
    complex_right_unbalanced.insert(18)
    assert complex_right_unbalanced.breadth_first_traversal() == [
        20, 10, 25, 18, 23, 30]


def test_delete_node_right_heavy_tree_self_balances(complex_right_unbalanced):
    """Test that the tree self balances when you delete a node."""
    complex_right_unbalanced.delete(10)
    assert complex_right_unbalanced.breadth_first_traversal() == [25, 20, 30]


def test_delete_root_right_heavy_tree_self_balances(complex_right_unbalanced):
    """Test that the tree self balances when you delete the root."""
    complex_right_unbalanced.delete(20)
    assert complex_right_unbalanced.breadth_first_traversal() == [25, 10, 30]


def test_deleting_node_after_insertion(complex_right_unbalanced):
    """Test that tree balances after insertion and delete."""
    complex_right_unbalanced.insert(23)
    complex_right_unbalanced.insert(18)
    complex_right_unbalanced.delete(20)
    assert complex_right_unbalanced.breadth_first_traversal() == [
        23, 10, 25, 18, 30]


def test_self_balancing_on_left_heavy_tree(complex_left_unbalanced):
    """Test that the tree self balances as you insert nodes."""
    assert complex_left_unbalanced.breadth_first_traversal() == [
        7, 5, 10, 6, 8, 15]


def test_adding_to_left_heavy_tree_self_balances(complex_left_unbalanced):
    """Test that the tree self balances when you add a new node."""
    complex_left_unbalanced.insert(13)
    complex_left_unbalanced.insert(11)
    assert complex_left_unbalanced.breadth_first_traversal() == [
        10, 7, 15, 5, 8, 13, 6, 11]


def test_deleting_node_from_left_heavy_tree_balances(complex_left_unbalanced):
    """Test that the tree balances when you delete a node."""
    complex_left_unbalanced.delete(5)
    assert complex_left_unbalanced.breadth_first_traversal() == [
        7, 6, 10, 8, 15]


def test_deleting_to_left_heavy_tree_self_balances(complex_left_unbalanced):
    """Test that the tree self balances when you delete the root."""
    complex_left_unbalanced.delete(7)
    assert complex_left_unbalanced.breadth_first_traversal() == [
        8, 5, 10, 6, 15]


def test_deletion_after_insertion_to_left_heavy_tree(complex_left_unbalanced):
    """Test that bst integrity is maintained after insertion and deletion."""
    complex_left_unbalanced.insert(13)
    complex_left_unbalanced.insert(11)
    complex_left_unbalanced.delete(5)
    assert complex_left_unbalanced.breadth_first_traversal() == [
        10, 7, 15, 6, 8, 13, 11]
