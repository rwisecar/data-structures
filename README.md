# Data Structures

# Linked List
##Module: linked_list.py
##Test Module: test_linked_list.py

This module consists of a Node class, which can be instantiated to create node instances. It also includes a LinkedList class, which can take a node as input, and create a linked list with that node as the head of the list. 

The module's *push()* method adds nodes to the list, connecting them to the list's head node, and creating a true linked list.

The module's *pop()* method removes the head of the list and returns it, and makes the next node the new head of the linked list.

The *size()* returns the length of the linked list, in number of nodes.

The *search()* method iterates through the linked list for a particular value and returns that value. If the value wasn't in the list, the method returns an error message.

The *remove()* method takes in a node, iterates through the list to find the node, removes it if it is present, and reattaches the pointer from the node before the deleted node to the node following the deleted node. 

The *display()* method accepts a linked list, and returns a string representing a tuple of the list values.

#Stack
##Module: stack.py
##Test Module: test_stack.py

The Stack module creates a stack that inherits some functionality from linked_list.py's LinkedList class via a constructor. 

It contains the size(), pop(), and push() functions, and is capable of taking both a dataset and a head value as input.


#Queue
##Module: queue.py
##Test Module: test_queue.py

The queue module creates a queue that inherits some functionality from dll.py-- the doubly linked list-- via a composition.

It contains the enqueue(), dequeue(), peek(), and size() methods, and follows the first in, first out format.


#Deque
##Module: deque.py
##Test Module: test_deque.py

The deque module creates a deque that inherits some functionality from the doubly linked list module via composition. Nodes can be added to, and removed from, both ends of the deque.

It contains the append(), appendleft(), pop(), popleft(), peek(), peekleft(), and size() methods. 


#Testing Information:

---------- coverage: platform darwin, python 2.7.13-final-0 ----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/deque.py                 24      0   100%
src/dll.py                   68      0   100%
src/linked_list.py           67      0   100%
src/queue.py                 22      0   100%
src/stack.py                 11      0   100%
src/test_deque.py            89      0   100%
src/test_dll.py              84      0   100%
src/test_linked_list.py      57      0   100%
src/test_queue.py            43      0   100%
src/test_stack.py            37      0   100%
-------------------------------------------------------
TOTAL                       502      0   100%


---------- coverage: platform darwin, python 3.5.2-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/deque.py                 24      0   100%
src/dll.py                   68      0   100%
src/linked_list.py           67      0   100%
src/queue.py                 22      0   100%
src/stack.py                 11      0   100%
src/test_deque.py            89      0   100%
src/test_dll.py              84      0   100%
src/test_linked_list.py      57      0   100%
src/test_queue.py            43      0   100%
src/test_stack.py            37      0   100%
-------------------------------------------------------
TOTAL                       502      0   100%
  py27: commands succeeded
  py35: commands succeeded


## We relied on the following resources in building our linked list and associated functions.

1. http://stackoverflow.com/questions/280243/python-linked-list
2. http://greenteapress.com/thinkpython/html/chap17.html
3. http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html
4. https://codefellows.github.io/sea-python-401d5/assignments/linked_list.html

We also received help from Claire and Amos! 