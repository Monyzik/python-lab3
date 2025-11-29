import random
from time import sleep

from src.algorithms.counting_sort import counting_sort
from src.benchmarks.benchmark_sorts import benchmark_sorts
from src.benchmarks.timeit_once import timeit_once
from src.constants import SORTS
from src.generators.rand_float_array import rand_float_array
from src.generators.rand_int_array import rand_int_array


def test_timeit_once():
    eps = 0.1
    def one_second() -> None:
        sleep(1)
    assert 1 - eps < timeit_once(one_second) < 1 + eps

def test_benchmark_sorts():
    arrays = dict((str(i), rand_int_array(random.randint(2, 100), -10, 100)) for i in range(10))
    ans = benchmark_sorts(dict(arrays), dict((sort.__name__, sort) for sort in SORTS))
    assert ans['1']['quick_sort'] >= 0
    arrays = {"1": rand_float_array(10)}
    ans = benchmark_sorts(arrays, {"counting": counting_sort})
    assert ans['1']['counting'] == -1