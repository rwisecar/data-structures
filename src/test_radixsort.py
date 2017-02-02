"""Tests for the radix sort."""
from radixsort import radix
import pytest


RADIX_PARAMS = [
    [[1], [1]],
    [[0], [0]],
    [[4, 6, 2, 3, 1, 5], [1, 2, 3, 4, 5, 6]],
    [[10000, 1, 500, 15, 4336, 0, 2982, 23, 5, 50],
        [0, 1, 5, 15, 23, 50, 500, 2982, 4336, 10000]],
    [[100, 100, 5, 5, 50, 50], [5, 5, 50, 50, 100, 100]],
]


@pytest.mark.parametrize("n, result", RADIX_PARAMS)
def test_radix_works_on_an_iterable_of_integers(n, result):
    """Test that you can radix sort a list of integers."""
    assert radix(n) == result


def test_radix_on_random_integers():
    """Test that radix sorts a list of random integers."""
    import random
    randos = [random.randint(0, 10000) for x in range(100)]
    new_list = radix(randos)
    for n in new_list[1:]:
        assert n > new_list[new_list.index(n) - 1]


def test_radix_sort_raises_error_with_nonintegers():
    """Test that radix raises a TypeError if you don't input integers."""
    with pytest.raises(TypeError):
        radix("abc")
