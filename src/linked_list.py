"""Create a linked_list class with assoc. methods and instantiate."""


class Node(object):
    """Create node instances that can populate the linked list."""
    def __init__(self, data=None, next_node=None):
        self.data = data
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
        return old_head.data

    def search(self, data):
        """Search through list for a node and return that node."""
        current = self.head
        found = False
        if self.length > 0:
            while current and found is False:
                if current.data == data:
                    found = True
                    return current
                else:
                    current = current.next_node
            if current is None:
                raise ValueError("Value not found in list.")
        return None

    # def remove(self, node):
    #     """Input a node and remove that node from the list."""
    #     if self.length > 0:
    #         head = self.head
    #         if node == head:
    #             return LinkedList(head.next, 1)
    #         current = head
    #         found = False
    #         while found is False:
    #             if current.next == node:
    #                 current.next = current.next.next
    #                 found is True
    #                 return LinkedList(head)
    #             current = current.next
    #         raise ValueError
    #     else:
    #         raise ValueError


"""Remove function found at codefellows.org"""
    # def delete(self, data):
    # current = self.head
    # previous = None
    # found = False
    # while current and found is False:
    #     if current.get_data() == data:
    #         found = True
    #     else:
    #         previous = current
    #         current = current.get_next()
    # if current is None:
    #     raise ValueError("Data not in list")
    # if previous is None:
    #     self.head = current.get_next()
    # else:
    #     previous.set_next(current.get_next())

    # def display()
