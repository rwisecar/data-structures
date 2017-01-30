"""Create a function to insertion-sort an iterable."""
from collections import Iterable


def insertion_sort(lst):
    """Insertion sort an iterable."""
    if isinstance(lst, Iterable):
        for idx in range(1, len(lst)):
            current = lst[idx]
            index = idx
            while index > 0 and lst[index - 1] > current:
                lst[index] = lst[index - 1]
                index -= 1
            lst[index] = current
        return lst
    else:
        raise TypeError("You cannot insertion_sort a non-iterable.")


# if __name__ == "__main__":
#     """Calculate the runtime for binary searches in the BST."""
#     import timeit
#     lst_1 = [50, 45, 60, 1, -59, 55, 70, -75, 65, 20, 48, 49, 0, 10, 25]
#     sortit = insertion_sort(lst_1)

#     sort_time = timeit.timeit(
#         stmt="balanced.search(75)",
#         setup="from __main__ import balanced",
#         number=1000
#     ) * 1000
#     unbal = timeit.timeit(
#         stmt="unbalanced.search(75)",
#         setup="from __main__ import unbalanced",
#         number=1000
#     ) * 1000
#     print("It takes {} microseconds to find 75 in a balanced tree, and {} microseconds to find 75 in an unbalanced tree".format(bal, unbal))

#     in_o = timeit.timeit(
#         stmt="balanced.in_order_traversal()",
#         setup="from __main__ import balanced",
#         number=1000
#     ) * 1000
#     pre = timeit.timeit(
#         stmt="balanced.pre_order_traversal()",
#         setup="from __main__ import balanced",
#         number=1000
#     ) * 1000
#     post = timeit.timeit(
#         stmt="balanced.post_order_traversal()",
#         setup="from __main__ import balanced",
#         number=1000
#     ) * 1000
#     breadth = timeit.timeit(
#         stmt="balanced.breadth_first_traversal()",
#         setup="from __main__ import balanced",
#         number=1000
#     ) * 1000

#     print("It takes {} microseconds to traverse tree in order\n It takes {} microseconds to traverse tree preorder\n It takes {} microseconds to traverse tree postorder\n It takes {} microseconds to traverse tree in breadth first\n ".format(in_o, pre, post, breadth))
