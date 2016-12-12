"""Create a linked_list class with assoc. methods and instantiate."""


class LinkedList(object):

    def __init__(self, head=None, length=0):
        """Create a linked list based on input nodes."""
        self.head = head
        self.length = length

    def __str__(self):
        return str(self.head)

    def push(self, val):
        """Add a node as the new head of a linked list."""
        node = Node(val)
        node.next = self.head
        self.head = node
        self.length = self.length + 1

    def pop(self):
        """Remove and return head of a linked list."""
        next_node = self.head.next
        old_head = self.head
        self.head = next_node
        self.length = self.length - 1
        return old_head

    def size(self):
        """Returns the length of the linked list."""
        return self.length

    # def search(val)

    # def remove(node)

    # def display()


class Node(object):
    """Create node instances that can populate the linked list."""
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val, self.next)

# # To make a new list from an old list
# new_list = [LinkedList(new_list[n]) for n in new_list]
