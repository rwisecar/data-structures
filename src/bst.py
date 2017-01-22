"""An implementation of a binary search tree."""


class Node(object):
    """Create node to for use in a binary search tree."""

    def __init__(self, value=None):
        """Create node to push into Doubly link list."""
        self.value = value
        self.left_child = None
        self.right_child = None

    def _the_children(self):
        children = []
        if self.left_child:
            children.append(self.left_child)
        if self.right_child:
            children.append(self.right_child)
        return children


class BST(object):
    """The Binary search tree class."""

    def __init__(self, iterable=None):
        """Initialize a binary search tree."""
        self.root = None
        self._size = 0
        if iterable and hasattr(iterable, "__iter__"):
            for i in iterable:
                self.insert(i)
        elif iterable:
            raise TypeError("Can't init with a non iterable.")

    def insert(self, value):
        """Insert value into the binary search tree."""
        if self.root:
            self._insert(value, self.root)
        else:
            self.root = Node(value)
            self._size += 1
        self.rebalance(self.root)

    def _insert(self, value, node):
        if value == node.value:
            pass
        elif value > node.value:
            if node.right_child:
                self._insert(value, node.right_child)
            else:
                node.right_child = Node(value)
                self._size += 1
        else:
            if node.left_child:
                self._insert(value, node.left_child)
            else:
                node.left_child = Node(value)
                self._size += 1

    def search(self, value):
        """Return the node containing val."""
        return self._search(value, self.root)

    def _search(self, value, node):
        if node.value == value:
            return node
        elif value > node.value:
            if node.right_child:
                return self._search(value, node.right_child)
            else:
                return None
        else:
            if node.left_child:
                return self._search(value, node.left_child)
            else:
                return None

    def size(self):
        """Return the size of the binary search tree."""
        return self._size

    def depth(self):
        """Return the depth of the binary search tree."""
        if not self.root:
            return -1
        else:
            return self._depth(self.root)

    def _depth(self, node):
        """Return actual depth utilizing _depth."""
        return self._depth_helper(node) - 1

    def _depth_helper(self, node):
        """Helper for depth method, returns depth plus one."""
        if node is None:
            return 0
        else:
            return max(self._depth_helper(node.left_child), self._depth_helper(node.right_child)) + 1

    def contains(self, value):
        """Return true if the val is contained in the BST, false otherwise."""
        return self._contains(value, self.root)

    def _contains(self, value, node):
        if node.value == value:
            return True
        elif value > node.value:
            if node.right_child:
                return self._contains(value, node.right_child)
            else:
                return False
        else:
            if node.left_child:
                return self._contains(value, node.left_child)
            else:
                return False

    def balance(self):
        """Return negative number if left leaning, postive for right leaning, or zero for balanced."""
        return self._balance(self.root)

    def _balance(self, node):
        """Return negative number if left leaning, postive for right leaning, or zero for balanced."""
        if node:
            right = self._depth(node.right_child)
            left = self._depth(node.left_child)
            return right - left
        return 0

    def in_order_traversal(self):
        """Traverse a BST ih order."""
        order = []
        result = self._traversal(self.root, 'inorder')
        for val in result:
            order.append(val.value)
        return order

    def pre_order_traversal(self):
        """Traverse a BST ih order."""
        order = []
        result = self._traversal(self.root, 'pre')
        for val in result:
            order.append(val.value)
        return order

    def post_order_traversal(self):
        """Traverse a BST ih order."""
        order = []
        result = self._traversal(self.root, 'post')
        for val in result:
            order.append(val.value)
        return order

    def _traversal(self, node, function):
        if node is None:
            return
        if function == "pre":
            yield node
        if node.left_child:
            for val in self._traversal(node.left_child, function):
                yield val
        if function == "inorder":
            yield node
        if node.right_child:
            for val in self._traversal(node.right_child, function):
                yield val
        if function == "post":
            yield node

    def breadth_first_traversal(self):
        """Traverse a BST ih order."""
        order = []
        result = self._breadth_first_traversal(self.root)
        for val in result:
            order.append(val.value)

        return order

    def _breadth_first_traversal(self, node):
        if node is None:
            return
        node_list = [node]
        while node_list:
            current = node_list.pop(0)
            yield current
            if current._the_children():
                for child in current._the_children():
                    node_list.append(child)

    def delete(self, val):
        """Delete a node while maintaining the integrity of the binary tree."""
        node, parent = self.root, None

        while node is not None and val != node.value:
            parent = node
            if val > node.value:
                node = node.right_child
            else:
                node = node.left_child

        if node is None:
            return None

        replacement = None

        # If node has two children
        if node.left_child and node.right_child:
            replacement = self._delete(node)
            replacement.left_child = node.left_child
            replacement.right_child = node.right_child
        # If node has one child or no children
        elif node.left_child is None:
            replacement = node.right_child
        else:
            replacement = node.left_child

        # Replace node
        if node == self.root:
            self.root = replacement
        elif parent.left_child == node:
            parent.left_child = replacement
        else:
            parent.right_child = replacement
        self.rebalance(self.root)
        self._size -= 1
        return None

    def _delete(self, node):
        """Hidden method to remove the node and fix pointers to children."""
        successor, parent = node.right_child, node
        while successor.left_child:
            parent = successor
            successor = successor.left_child

        # If there are no more left children
        if successor == parent.right_child:
            parent.right_child = successor.right_child
        else:
            parent.left_child = successor.right_child
        return successor

    def rebalance(self, node):
        """Rebalance tree and call rotate methods."""
        while self._balance(node) < -1 or self._balance(node) > 1:
            # import pdb; pdb.set_trace()
            if self._balance(node) > 1:
                if self._balance(node.right_child) < 0:
                    self.rotate_right(node.right_child, node)
                    self.rotate_left(node)
                else:
                    self.rotate_left(node)
            if self._balance(node) < -1:
                if self._balance(node.left_child) > 0:
                    self.rotate_left(node.left_child, node)
                    self.rotate_right(node)
                else:
                    self.rotate_right(node)

    def rotate_left(self, node, parent=None):
        """Rotate node left."""
        new_root = node.right_child
        new_left_sub = new_root.left_child
        old_root = node
        node = new_root
        old_root.right_child = new_left_sub
        new_root.left_child = old_root
        if parent:
            parent.left_child = new_root
        else:
            self.root = new_root

    def rotate_right(self, node, parent=None):
        """Rotate node right."""
        new_root = node.left_child
        new_left_sub = new_root.right_child
        old_root = node
        node = new_root
        old_root.left_child = new_left_sub
        new_root.right_child = old_root
        if parent:
            parent.right_child = new_root
        else:
            self.root = new_root


if __name__ == "__main__":
    bst = BST([10, 20, 30, 25])
    bst = BST([10, 15, 7, 5, 8, 6])
    # bst = BST([6, 2, 7, 1, 4, 8, 3, 5, 9])
    print(bst.breadth_first_traversal())
    bst.delete(5)
    print(bst.breadth_first_traversal())
    bst.delete(6)
    print(bst.breadth_first_traversal())
    # """Calculate the runtime for binary searches in the BST."""
    # import timeit
    # value = [50, 45, 60, 58, 59, 55, 70, 75, 65, 20, 48, 49, 46, 10, 25]
    # balanced = BST(value)
    # unbalanced = BST(sorted(value))

    # bal = timeit.timeit(
    #     stmt="balanced.search(75)",
    #     setup="from __main__ import balanced",
    #     number=1000
    # ) * 1000
    # unbal = timeit.timeit(
    #     stmt="unbalanced.search(75)",
    #     setup="from __main__ import unbalanced",
    #     number=1000
    # ) * 1000
    # print("It takes {} microseconds to find 75 in a balanced tree, and {} microseconds to find 75 in an unbalanced tree".format(bal, unbal))

    # in_o = timeit.timeit(
    #     stmt="balanced.in_order_traversal()",
    #     setup="from __main__ import balanced",
    #     number=1000
    # ) * 1000
    # pre = timeit.timeit(
    #     stmt="balanced.pre_order_traversal()",
    #     setup="from __main__ import balanced",
    #     number=1000
    # ) * 1000
    # post = timeit.timeit(
    #     stmt="balanced.post_order_traversal()",
    #     setup="from __main__ import balanced",
    #     number=1000
    # ) * 1000
    # breadth = timeit.timeit(
    #     stmt="balanced.breadth_first_traversal()",
    #     setup="from __main__ import balanced",
    #     number=1000
    # ) * 1000

    # print("It takes {} microseconds to traverse tree in order\n It takes {} microseconds to traverse tree preorder\n It takes {} microseconds to traverse tree postorder\n It takes {} microseconds to traverse tree in breadth first\n ".format(in_o, pre, post, breadth))
