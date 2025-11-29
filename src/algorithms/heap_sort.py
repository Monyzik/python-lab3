from functools import cmp_to_key
from typing import TypeVar, Callable, Any

from src.exceptions import CmpAndKeyTogetherException
from src.structures.binary_heap import BinaryHeap

T = TypeVar('T')


def heap_sort(a: list[T], key: Callable[[T], Any] | None = None, cmp: Callable[[T, T], int] | None = None) -> list[T]:
    """
    Сортировка кучей О(n * log(n))
    :param a: Массив объектов, который необходимо отсортировать.
    :param key: Ключ по которому будет производиться сортировка (по умолчанию сортирует по возрастанию)
    :param cmp: оператор сравнения (переводится в key)
    :return: Возвращает отсортированный по ключу массив
    """
    if key is not None and cmp is not None:
        raise CmpAndKeyTogetherException(heap_sort)
    if cmp is not None:
        key = cmp_to_key(cmp)
    if key is None:
        key = lambda x: x

    answer = []
    heap = BinaryHeap(a, key)
    for i in range(len(a)):
        answer.append(heap.extract())
    return answer
