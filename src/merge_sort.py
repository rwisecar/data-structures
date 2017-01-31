"""Sort a list using the merge sort method."""


def merge_sort(lst):
    """Sort a list using the merge sort method.
    Break the list up into n components each with one element.
    Sort and merge using the _merge helper function.
    """
    if len(lst) < 2:
        return lst
    midpoint_idx = len(lst)/2
    first_half = merge_sort(lst[:midpoint_idx])
    second_half = merge_sort(lst[midpoint_idx:])
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
