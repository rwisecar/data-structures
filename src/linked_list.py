"""Create a linked_list class with assoc. methods and instantiate."""


class Node(object):
    """Create node instances that can populate the linked list."""
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList(object):

    def __init__(self, head=None, data=None, length=0):
        """Create a linked list based on input nodes."""
        self.length = length
        # self.head = None
        if data:
            try:
                for item in data:
                    if item is data[0]:
                        self.head = Node(item)
                    else:
                        self.head = Node(item, self.head)
            except TypeError:
                self.head = Node(data)
        else:
            self.head = head
        # if data:
        #     try:
        #         for d in data:
        #             if d is data[0]:
        #                 self.head = Node(d)
        #             else:
        #                 self.head = Node(d, self.head)
        #     except TypeError:
        #         self.head = Node(data)
        # self.head = head

#     def push(self, val):
#         """Add a node as the new head of a linked list."""
#         node = Node(val)
#         node.next = self.head
#         self.head = node
#         self.length = self.length + 1

#     def pop(self):
#         """Remove and return head of a linked list."""
#         next_node = self.head.next
#         old_head = self.head
#         self.head = next_node
#         self.length = self.length - 1
#         return old_head.val

#     def size(self):
#         """Return the length of the linked list."""
#         return self.length

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

    # def search(self, value):
    #     """Search through list for a node and return that node."""
    #     current = self.head
    #     found = False
    #     if self.length > 0:
    #         while found is False:
    #             if current.val == value:
    #                 found = True
    #                 return current
    #             current = current.next
    #         return None
    #     return None

"""Search function found at https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/"""
    # def search(self, data):
    # current = self.head
    # found = False
    # while current and found is False:
    #     if current.get_data() == data:
    #         found = True
    #     else:
    #         current = current.get_next()
    # if current is None:
    #     raise ValueError("Data not in list")
    # return current

    # def display()
