from functools import cmp_to_key
from typing import TypeVar, Callable, Any

from src.structures.binary_heap import BinaryHeap

T = TypeVar('T')


def heap_sort(a: list[T], key: Callable[[T], Any] | None = None, cmp: Callable[[T, T], int] | None = None) -> list[T]:
    """
    Сортировка кучей
    :param a: Массив объектов, который необходимо отсортировать.
    :param key: Ключ по которому будет производиться сортировка (по умолчанию сортирует по возрастанию)
    :param cmp: оператор сравнения (переводится в key)
    :return: Возвращает отсортированный по ключу массив
    """
    if key is not None and cmp is not None:
        raise ValueError("Невозможно отсортировать по cmp и key одновременно")
    if cmp is not None:
        key = cmp_to_key(cmp)
    if key is None:
        key = lambda x: x

    answer = []
    heap = BinaryHeap(a, key)
    for i in range(len(a)):
        answer.append(heap.extract())
    return answer


print(heap_sort([10000, -2, 5, 4, 3, 2, 1, 0]))
print(heap_sort([(10000, -2), (5, 4), (3, 2), (1, 100)], key=lambda x: (x[1], x[0])))


def cmp(a, b):
    if a[1] == b[1]:
        return a[0] > b[0]
    return a[1] > b[1]


print(heap_sort([(10000, -2), (5, 4), (3, 2), (1, 100)], cmp=cmp))
