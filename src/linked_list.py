"""Create a linked_list class with assoc. methods and instantiate."""


class Node(object):
    """Create node instances that can populate the linked list."""
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList(object):

    def __init__(self, head=None, data=None):
        """Create a linked list based on input nodes."""
        self.length = 0
        self.head = None

        if data and hasattr(data, "__iter__"):
            for item in data:
                self.push(item)
        elif data:
            raise TypeError
        elif head and not data:
            self.push(head)

    def size(self):
        """Return the length of the linked list."""
        return self.length

    def push(self, value):
        """Add a node as the head of a linked list."""
        new_node = Node(value)
        if self.head:
            new_node.next_node = self.head
            new_node = Node(value, self.head)
            self.head = new_node
        else:
            self.head = new_node
        self.length += 1

    def pop(self):
        """Remove and return head of a linked list."""
        if self.head is None:
            raise IndexError("Cannot pop from an empty list.")
        next_node = self.head.next_node
        old_head = self.head
        self.head = next_node
        self.length = self.length - 1
        return old_head.value

    def search(self, val):
        """Search through list for a node and return that node."""
        current = self.head
        found = False
        if self.length > 0:
            while current and found is False:
                if current.value == val:
                    found = True
                    return current
                else:
                    current = current.next_node
            if current is None:
                raise ValueError("Value not found in list.")

    def display(self):
        """Input a linked list and return a string showing list in tuples."""
        linked_list_string = "("
        current = self.head
        while current:
            linked_list_string += "{}, ".format(str(current))
            current = current.next_node
        linked_list_string += ")"
        return linked_list_string

    def remove(self, node):
        """Input a node and remove that node from the list."""
        current = self.head
        previous = None
        try:
            while current:
                if current == node:
                    break
                else:
                    previous = current
                    current = previous.next_node
            if previous is None:
                self.head = current.next_node()
            else:
                previous.next_node = current.next_node
            self.length -= 1
        except ValueError:
            raise ValueError("Node not found in list.")
