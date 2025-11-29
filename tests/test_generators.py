from collections import Counter

import pytest

from src.exceptions import NegativeNumberException
from src.generators.reverse_sorted import reverse_sorted
from src.generators.many_duplicates import many_duplicates
from src.generators.nearly_sorted import nearly_sorted
from src.generators.rand_float_array import rand_float_array
from src.generators.rand_int_array import rand_int_array


def test_seeds():
    assert many_duplicates(10, seed=1534) == many_duplicates(10, seed=1534)
    assert nearly_sorted(10, 4, seed=1534) == nearly_sorted(10, 4, seed=1534)
    assert rand_int_array(10, 1, 10, seed=1534) == rand_int_array(10, 1, 10, seed=1534)
    assert rand_float_array(10, seed=1534) == rand_float_array(10, seed=1534)


def test_lower_bigger_height_error():
    with pytest.raises(ValueError):
        rand_int_array(10, 10, 1)
    with pytest.raises(ValueError):
        rand_float_array(10, 10, 1)


def test_negative_error():
    with pytest.raises(NegativeNumberException):
        rand_int_array(-1, 10, 11)
    with pytest.raises(NegativeNumberException):
        rand_float_array(-1)
    with pytest.raises(NegativeNumberException):
        nearly_sorted(-1, 1)
    with pytest.raises(NegativeNumberException):
        many_duplicates(-1)
    with pytest.raises(NegativeNumberException):
        reverse_sorted(-1)


def test_distinct_random_int():
    a = rand_int_array(10, 10, 100, distinct=True)
    assert all([x == 1 for x in Counter(a).values()])


def test_bad_diapason_for_random_int():
    with pytest.raises(ValueError):
        rand_int_array(10, 10, 18, distinct=True)
