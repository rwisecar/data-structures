"""A function that sorts a list using the quicksort method."""


def quicksort(lst):
    """Sort a list using the quicksort method."""
    if len(lst) < 2:
        return lst
    elif isinstance(lst, list):
        first_half = []
        second_half = []
        pivot = lst[len(lst) // 2]
        for item in lst:
            if item < pivot:
                first_half.append(item)
            elif item is pivot:
                continue
            else:
                second_half.append(item)
        return quicksort(first_half) + [pivot] + quicksort(second_half)

    else:
        raise TypeError("You may only sort a list.")


if __name__ == "__main__":
    import timeit
    import random

    lst_1 = [1]
    lst_2 = [x for x in range(100)][::-1]
    lst_3 = [random.randint(0, 100) for x in range(100)]

    best_case = timeit.timeit(
        stmt="quicksort(lst_1)",
        setup="from __main__ import quicksort, lst_1",
        number=1000
    ) * 1000

    worst_case = timeit.timeit(
        stmt="quicksort(lst_2)",
        setup="from __main__ import quicksort, lst_2",
        number=1000
    ) * 1000

    average_case = timeit.timeit(
        stmt="quicksort(lst_3)",
        setup="from __main__ import quicksort, lst_3",
        number=1000
    ) * 1000

    print("Quicksort's best case scenario takes {} microseconds.\n Quicksort's average case scenario takes {} microseconds.\n Quicksort's worst case scenario takes {} microseconds.".format(best_case, average_case, worst_case))
