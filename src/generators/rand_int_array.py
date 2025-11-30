import random

from src.exceptions import NegativeNumberException


def rand_int_array(n: int, lo: int, hi: int, *, distinct: bool = False, seed=None) -> list[int]:
    """
    Генерирует случайный массив целых чисел из диапазона [lo, hi].
    :param n: Размер массива.
    :param lo: Нижняя граница генерации.
    :param hi: Верхняя граница генерации.
    :param distinct: Флаг, если указан, то генерируются уникальные числа.
    :param seed: Параметр генерации.
    :return: Возвращает случайный массив целых чисел из диапазона [lo, hi].
    """
    if n < 0:
        raise NegativeNumberException(rand_int_array)
    if lo > hi:
        raise ValueError(f"Нижняя граница не может быть больше верхней")
    if distinct and hi - lo + 1 < n:
        raise ValueError(f"Невозможно сгенерировать n различных элементов в диапазоне [{lo}, {hi}]")
    if seed:
        random.seed(seed)
    if distinct:
        return random.sample(range(lo, hi + 1), n)
    return [random.randint(lo, hi) for _ in range(n)]
