# Data Structures

[![Build Status](https://travis-ci.org/rwisecar/data-structures.svg?branch=master)](https://travis-ci.org/rwisecar/data-structures)

[![Coverage Status](https://coveralls.io/repos/github/rwisecar/data-structures/badge.svg)](https://coveralls.io/github/rwisecar/data-structures)

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

#Binary Heap
##Module: binheap.py
##Test Module: text_deque.py

The binary heap module creates a minheap binary heap structure, in which each parent is smaller than its child elements. It has a pop() method, which removes the first element and maintains the heap structure, and a push() method, which adds an element to the end and resorts the structure as necessary.

We refactored this module after reviewing Maelle and Ben S.'s code in class. We also looked at https://interactivepython.org/runestone/static/pythonds/Trees/BinaryHeapImplementation.html 

#Priority Queue
##Module: priority_queue.py
##Test Module: test_priority_queue.py

The priority queue takes in a list of tuples of (value, priority). 

The insert(value, priority=0) method adds an item to the queue with the value and priority assigned by the user. The pop() method returns the tuple with the lowest priority (most important item). The peek()function returns the value of the most important item, without removing it.

We had help from the following stack overflow resource: http://stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value

#Graph
##Module: graph.py
##Test Module: test_graph.py

Our graph structure creates an weighted, directed graph in which nodes have edges connecting them to other nodes. We built our graph using a series of dictionaries. The associated methods are as follows.

For the depth and breadth traversal methods, we used the following resources:
Claire
http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
http://codereview.stackexchange.com/questions/78577/depth-first-search-in-python

### Methods:

    The nodes(): returns a list of all nodes in the graph.

    edges(): returns a list of all edges in the graph.

    add_node(n): adds a new node, n, to the graph.

    add_edge(n1, n2): adds n1 and n2 if they don't exist, and adds an edge connecting them.

    del_node(n): deletes node n from the graph.

    del_edge(n1, n2): deletes the edge connecting n1 and n2.

    has_node(n): Returns True if node n is contained in the graph.

    neighbors(n): Returns a list of all nodes connected to n by edges.

    adjacent(n1, n2): returns True if n1 and n2 are connceted by an edge.

    depth_traversal(start, checked=none): returns the path traversed by depth.

    breadth_traversal(start): traverses the graph by breadth and returns the path.
    """
---

#Binary Search Tree
##Module: bst.py
##Test Module: test_bst.py

The binary search tree takes in an iterable that will populate the tree using Nodes that consist of the Node Value, and pointers to the left and right children of that node.  Any left child must be smaller than its parent node and and right child myust be greater than its parent node.

We had help from the following resources: 
1. http://stackoverflow.com/questions/19187901/counting-number-of-nodes-in-a-binary-search-tree
2. http://stackoverflow.com/questions/29379213/depth-of-a-binary-search-tree-in-python
3. https://interactivepython.org/courselib/static/pythonds/Trees/SearchTreeImplementation.html
4. http://stackoverflow.com/questions/33301591/binary-tree-inorder-traversal-using-generator

### BST Methods:
    insert(self, val): will insert the value val into the BST. If val is already present, it will be ignored.

    search(self, val): will return the node containing that value, else None

    size(self): will return the integer size of the BST (equal to the total number of values stored in the tree). It will return 0 if the tree is empty.

    depth(self): will return an integer representing the total number of levels in the tree. If there is one value, the depth should be 1, if two values it will be 2, if three values it may be 2 or three, depending, etc.

    contains(self, val): will return True if val is in the BST, False if not.

    balance(self): will return an integer, positive or negative that represents how well balanced the tree is. Trees which are higher on the left than the right should return a positive value, trees which are higher on the right than the left should return a negative value. An ideally-balanced tree should return 0.

#Testing Information:
```
---------- coverage: platform darwin, python 2.7.10-final-0 ----------
Name                         Stmts   Miss  Cover   Missing
----------------------------------------------------------
src/binheap.py                  30      0   100%
src/deque.py                    24      0   100%
src/dll.py                      68      0   100%
src/graph.py                    80     12    85%   122-143
src/linked_list.py              67      0   100%
src/priority_queue.py           20      0   100%
src/queue.py                    22      0   100%
src/stack.py                    11      0   100%
src/test_binheap.py             40      0   100%
src/test_deque.py               89      0   100%
src/test_dll.py                 84      0   100%
src/test_graph.py              163      0   100%
src/test_linked_list.py         57      0   100%
src/test_priority_queue.py      53      0   100%
src/test_queue.py               43      0   100%
src/test_stack.py               37      0   100%
----------------------------------------------------------
TOTAL                          888     12    99%


---------- coverage: platform darwin, python 3.5.2-final-0 -----------
Name                         Stmts   Miss  Cover   Missing
----------------------------------------------------------
src/binheap.py                  30      0   100%
src/deque.py                    24      0   100%
src/dll.py                      68      0   100%
src/graph.py                    80     12    85%   122-143
src/linked_list.py              67      0   100%
src/priority_queue.py           20      0   100%
src/queue.py                    22      0   100%
src/stack.py                    11      0   100%
src/test_binheap.py             40      0   100%
src/test_deque.py               89      0   100%
src/test_dll.py                 84      0   100%
src/test_graph.py              163      0   100%
src/test_linked_list.py         57      0   100%
src/test_priority_queue.py      53      0   100%
src/test_queue.py               43      0   100%
src/test_stack.py               37      0   100%
----------------------------------------------------------
TOTAL                          888     12    99%


  py27: commands succeeded
  py35: commands succeeded
```

## We relied on the following resources in building our linked list and associated functions.

1. http://stackoverflow.com/questions/280243/python-linked-list
2. http://greenteapress.com/thinkpython/html/chap17.html
3. http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html
4. https://codefellows.github.io/sea-python-401d5/assignments/linked_list.html

We also received help from Claire and Amos! 
