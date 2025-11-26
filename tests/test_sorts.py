import random

import pytest

from src.constants import SORTS
from src.generators.many_duplicates import many_duplicates
from src.generators.nearly_sorted import nearly_sorted
from src.generators.rand_int_array import rand_int_array
from src.generators.reverse_sorted import reverse_sorted


@pytest.mark.repeat(10)
@pytest.mark.parametrize("func", [*SORTS])
def test_sorts(func):
    n = random.randint(0, 1000)
    arr = rand_int_array(n, -100, 100)
    assert func(arr) == sorted(arr)
    arr = many_duplicates(n)
    assert func(arr) == sorted(arr)
    arr = nearly_sorted(n, random.randint(0, n))
    assert func(arr) == sorted(arr)
    arr = reverse_sorted(n)
    assert func(arr) == sorted(arr)


def test_sorts_invalid_arguments():
    pass
