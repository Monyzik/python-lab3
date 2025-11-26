from functools import cmp_to_key
from random import randint
from typing import Any, Callable, TypeVar

from src.exceptions import CmpAndKeyTogetherException

T = TypeVar('T')


def quick_sort(a: list[T],
               key: Callable[[T], Any] | None = None,
               cmp: Callable[[T, T], int] | None = None) -> list[T]:
    """
    Быстрая сортировка (О(n * log(n)))
    :param a: Массив объектов, который необходимо отсортировать.
    :param key: Ключ по которому будет производиться сортировка (по умолчанию сортирует по возрастанию)
    :param cmp: оператор сравнения (переводится в key)
    :return: Возвращает отсортированный по ключу массив
    """

    if key is not None and cmp is not None:
        raise CmpAndKeyTogetherException(key)
    if cmp is not None:
        key = cmp_to_key(cmp)
        cmp = None
    if key is None:
        key = lambda x: x

    if len(a) <= 1:
        return a
    value = key(a[randint(0, len(a) - 1)])
    less = [x for x in a if key(x) < value]
    equal = [x for x in a if key(x) == value]
    greater = [x for x in a if key(x) > value]
    return quick_sort(less, key=key, cmp=cmp) + equal + quick_sort(greater, key=key, cmp=cmp)

# print(quick_sort([10000, -2, 5, 4, 3, 2, 1, 0]))
# print(quick_sort([(10000, -2), (5, 4), (3, 2), (1, 100)], key=lambda x: True))
# print(sorted([(10000, -2), (5, 4), (3, 2), (1, 100)], key=lambda x: True))
#
#
# def cmp(a, b):
#     return a[1] - b[1]
#     if a[1] == b[1]:
#         return a[0] > b[0]
#     return a[1] > b[1]
#
#
# print(quick_sort([(10000, -2), (5, 4), (3, 2), (1, 100)], cmp=cmp))
