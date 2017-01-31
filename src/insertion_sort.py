"""Create a function to insertion-sort an iterable."""


def insertion_sort(lst):
    """Insertion sort an iterable."""
    if isinstance(lst, list):
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


if __name__ == "__main__":
    """Calculate the runtime for binary searches in the BST."""
    import timeit
    import random
    lst_1 = [random.randint(-100, 100) for x in range(10000)]
    lst_2 = [1, 2, 3]
    lst_3 = [x for x in range(10000)][::-1]

    best_case = timeit.timeit(
        stmt="insertion_sort(lst_2)",
        setup="from __main__ import insertion_sort, lst_2",
        number=1000
    ) * 1000

    average_case = timeit.timeit(
        stmt="insertion_sort(lst_1)",
        setup="from __main__ import insertion_sort, lst_1",
        number=1000
    ) * 1000

    worst_case = timeit.timeit(
        stmt="insertion_sort(lst_3)",
        setup="from __main__ import insertion_sort, lst_3",
        number=1000
    ) * 1000

    print("Insertion sort's best case scenario takes {} microseconds.\n Insertion sort's average case scenario takes {} microseconds.\n Insertion sort's worst case scenario takes {} microseconds.".format(best_case, average_case, worst_case))

