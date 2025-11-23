import copy
from functools import cmp_to_key
from typing import Callable, Any, TypeVar

T = TypeVar('T')


def bubble_sort(a: list[T],
                key: Callable[[T], Any] | None = None,
                cmp: Callable[[T, T], int] | None = None) -> list[T]:
    """
    Сортировка пузырьком (О(n ^ 2))
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

    result = copy.deepcopy(a)
    length = len(result)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if key(result[j]) > key(result[j + 1]):
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


print(bubble_sort([-1, 5, 4, 3, 2, 1, -2]))
print(bubble_sort([-1, 5, 4, 3, 2, 1, -2], key=lambda x: -x))
