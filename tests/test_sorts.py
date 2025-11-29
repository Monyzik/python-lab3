import random

import pytest

from functools import cmp_to_key

from src.cli import sort_cli, loop
from src.exceptions import CmpAndKeyTogetherException
from src.algorithms.bubble_sort import bubble_sort
from src.algorithms.heap_sort import heap_sort
from src.algorithms.quick_sort import quick_sort
from src.algorithms.bucket_sort import bucket_sort
from src.algorithms.radix_sort import radix_sort
from src.exceptions import NegativeNumberException
from src.constants import SORTS, SORTS_NAMES
from src.generators.rand_float_array import rand_float_array
from src.generators.many_duplicates import many_duplicates
from src.generators.nearly_sorted import nearly_sorted
from src.generators.rand_int_array import rand_int_array
from src.generators.reverse_sorted import reverse_sorted


@pytest.mark.repeat(5)
@pytest.mark.parametrize("sort_name, func", SORTS_NAMES.items())
def test_sorts(sort_name, func):
    n = random.randint(2, 100)
    arr = rand_int_array(n, -10000, 10000)
    assert func(arr) == sorted(arr)
    arr = many_duplicates(n)
    assert func(arr) == sorted(arr)
    arr = nearly_sorted(n, random.randint(0, n))
    assert func(arr) == sorted(arr)
    arr = reverse_sorted(n)
    assert func(arr) == sorted(arr)
    loop.command(sort_name, arr, 2, 2)


def test_sorts_invalid_arguments():
    with pytest.raises(NegativeNumberException):
        bucket_sort([-1], buckets=-1)
    with pytest.raises(NegativeNumberException):
        radix_sort([-1], base=-1)
    with pytest.raises(ValueError):
        radix_sort([-1], base=1)


@pytest.mark.parametrize("func", [quick_sort, bubble_sort, heap_sort])
def test_key_in_sorts(func):
    n = random.randint(0, 1000)
    arr = rand_int_array(n, -100, 100)
    key = lambda x: -x
    assert func(arr, key=key) == sorted(arr, key=key)


@pytest.mark.parametrize("func", [quick_sort, bubble_sort, heap_sort])
def test_cmp_in_sorts(func):
    n = random.randint(0, 1000)
    arr = rand_int_array(n, 1, 2)

    def cmp(a, b):
        a &= 1
        b &= 1
        return a - b

    assert func(arr, cmp=cmp) == sorted(arr, key=cmp_to_key(cmp))


@pytest.mark.parametrize("func", [quick_sort, bubble_sort, heap_sort])
def test_cmp_and_key_in_sorts(func):
    cmp = lambda x, y: y - x
    key = lambda x: -x
    with pytest.raises(CmpAndKeyTogetherException):
        func([-1], key=key, cmp=cmp)


@pytest.mark.repeat(5)
@pytest.mark.parametrize("func", [bucket_sort, quick_sort, heap_sort, bubble_sort])
def test_float_sorts(func):
    n = random.randint(0, 1000)
    arr = rand_float_array(n, -100, 100)
    assert func(arr) == sorted(arr)
