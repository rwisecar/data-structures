"""Create a function to insertion-sort an iterable."""


def insertion_sort(lst):
    """Insertion sort an iterable."""
    for idx in range(1, len(lst)):
        current = lst[idx]
        index = idx
        while index > 0 and lst[index - 1] > current:
            lst[index] = lst[index - 1]
            index -= 1
        lst[index] = current
    return lst


if 