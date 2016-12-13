"""Create a linked_list class with assoc. methods and instantiate."""


class LinkedList(object):

    def __init__(self, head=None, length=0):
        """Create a linked list based on input nodes."""
        self.head = head
        self.length = length

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
        return old_head.val

    def size(self):
        """Return the length of the linked list."""
        return self.length

    def remove(self, node):
        """Input a node and remove that node from the list."""
        if self.length > 0:
            head = self.head
            if node == head:
                return LinkedList(head.next, 1)
            current = head
            found = False
            while found is False:
                if current.next == node:
                    current.next = current.next.next
                    found is True
                    return LinkedList(head)
                current = current.next
            raise ValueError
        else:
            raise ValueError

    def search(self, value):
        """Search through list for a node and return that node."""
        current = self.head
        found = False
        if self.length > 0:
            while found is False:
                if current.val == value:
                    found = True
                    return current
                current = current.next
            return None
        return None

    def display()


class Node(object):
    """Create node instances that can populate the linked list."""
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
