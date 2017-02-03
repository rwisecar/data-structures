"""Sort a list using the merge sort method."""


def merge_sort(lst):
    """Sort a list using the merge sort method.
    Break the list up into n components each with one element.
    Sort and merge using the _merge helper function.
    """
    if len(lst) < 2:
        return lst
    midpoint_idx = len(lst)//2
    first_half = merge_sort(lst[midpoint_idx:])
    second_half = merge_sort(lst[:midpoint_idx])
    return _merge(first_half, second_half)


def _merge(first_half, second_half):
    """Merge the sorted lists together."""
    if not first_half:
        return second_half
    if not second_half:
        return first_half
    if first_half[0] < second_half[0]:
        return [first_half[0]] + _merge(first_half[1:], second_half)
    return [second_half[0]] + _merge(first_half, second_half[1:])


if __name__ == "__main__":
    import timeit
    import random

    lst_1 = [1]
    lst_2 = [x for x in range(100)][::-1]
    lst_3 = [random.randint(0, 100) for x in range(100)]

    best_case = timeit.timeit(
        stmt="merge_sort(lst_1)",
        setup="from __main__ import merge_sort, lst_1",
        number=1000
    ) * 1000

    worst_case = timeit.timeit(
        stmt="merge_sort(lst_2)",
        setup="from __main__ import merge_sort, lst_2",
        number=1000
    ) * 1000

    average_case = timeit.timeit(
        stmt="merge_sort(lst_3)",
        setup="from __main__ import merge_sort, lst_3",
        number=1000
    ) * 1000

    print("Merge sort's best case scenario takes {} microseconds.\n Merge sort's average case scenario takes {} microseconds.\n Merge sort's worst case scenario takes {} microseconds.".format(best_case, average_case, worst_case))
