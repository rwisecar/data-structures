"""A function that sorts a list of numbers using the radix method."""


def radix(lst):
    """Sort a list of numbers using the radix sort method."""
    for num in lst:
        if not isinstance(num, int):
            raise TypeError('Must use integers')
    digit_place = 1
    number_of_places, working_num = 0, 0
    new_lst = lst
    while number_of_places < len(str(max(lst))) + 1:
        buckets = [[] for _ in range(10)]
        for num in new_lst:
            working_num = num // digit_place
            buckets[working_num % 10].append(num)
        new_lst = []
        for b in buckets:
            for num in b:
                new_lst.append(num)

        digit_place *= 10
        number_of_places += 1
    return new_lst


if __name__ == "__main__":
    import timeit
    import random

    lst_1 = [1]
    lst_2 = [x for x in range(100)][::-1]
    lst_3 = [random.randint(0, 100) for x in range(100)]

    best_case = timeit.timeit(
        stmt="radix(lst_1)",
        setup="from __main__ import radix, lst_1",
        number=1000
    ) * 1000

    worst_case = timeit.timeit(
        stmt="radix(lst_2)",
        setup="from __main__ import radix, lst_2",
        number=1000
    ) * 1000

    average_case = timeit.timeit(
        stmt="radix(lst_3)",
        setup="from __main__ import radix, lst_3",
        number=1000
    ) * 1000

    print("radix's best case scenario takes {} microseconds.\n radix's average case scenario takes {} microseconds.\n radix's worst case scenario takes {} microseconds.".format(best_case, average_case, worst_case))
