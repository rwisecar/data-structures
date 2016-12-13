"""Create a linked_list class with assoc. methods and instantiate."""


class Node(object):
    """Create node instances that can populate the linked list."""
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList(object):

    def __init__(self, head=None, data=None, length=0):
        """Create a linked list based on input nodes."""
        if data:
            try:
                for item in data:
                    if item is data[0]:
                        self.head = Node(item)
                        self.length = 1
                    else:
                        self.head = Node(item, self.head)
                        self.length += 1
            except TypeError:
                self.head = Node(data)
        else:
            self.head = head
            self.length = length

    def size(self):
        """Return the length of the linked list."""
        return self.length

    def push(self, data):
        """Add a node as the new head of a linked list."""
        node = Node(data)
        node.next_node = self.head
        self.head = node
        self.length = self.length + 1

    def pop(self):
        """Remove and return head of a linked list."""
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
        return None

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
        found = False
        while current and found is False:
            # import pdb;pdb.set_trace()
            if current == node:
                if previous is None:
                    self.head = current.next_node()
                else:
                    previous.next_node = current.next_node
                self.length -= 1
                found = True
            previous = current
            current = previous.next_node
        # if current is None:
        #     raise ValueError("Node not found in list.")
