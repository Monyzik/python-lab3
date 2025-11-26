import time

from src.algorithms.counting_sort import counting_sort
from src.algorithms.heap_sort import heap_sort
from src.algorithms.quick_sort import quick_sort
from src.algorithms.radix_sort import radix_sort
from src.generators.rand_int_array import rand_int_array


def timeit_once(func, *args, **kwargs) -> float:
    """
    Считает время выполнения func, запущенной один раз.
    :param func: Функция, время которой засекается.
    :param args: Неименованные аргументы функции.
    :param kwargs: Именованные аргументы функции.
    :return: Возвращает время работы func.
    """
    start = time.perf_counter()
    func(*args, **kwargs)
    end = time.perf_counter()
    return end - start

# print(timeit_once(heap_sort, rand_int_array(10000000, -10000000, 10000000)))
# print(timeit_once(counting_sort, rand_int_array(10000000, -10000000, 10000000)))
