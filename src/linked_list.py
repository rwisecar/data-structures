"""Create a linked_list class with assoc. methods and instantiate."""

class LinkedList(object):

    def __init__(self, cargo=None, next=None, new_list=None):
        if new_list is None:
            self.cargo = cargo
            self.next = next
            self.new_list = []
        # To make a new list from an old list
        new_list = [LinkedList(new_list[n]) for n in new_list]

    def __str__(self):
        return str(self.cargo)

    # def push(val)

    # def pop()

    # def size()

    # def search(val)

    # def remove(node)

    # def display()
