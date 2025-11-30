import random

from src.exceptions import NegativeNumberException


def rand_float_array(n: int, lo=0.0, hi=1.0, *, seed=None) -> list[float]:
    """
    Генерирует случайный массив вещественных чисел из диапазона [lo, hi].
    :param n: Размер массива.
    :param lo: Нижняя граница генерации.
    :param hi: Верхняя граница генерации.
    :param seed: Параметр генерации.
    :return: Возвращает случайный массив вещественных чисел из диапазона [lo, hi].
    """
    if n < 0:
        raise NegativeNumberException(rand_float_array)
    if lo > hi:
        raise ValueError(f"Нижняя граница не может быть больше верхней")
    if seed is not None:
        random.seed(seed)
    return [random.uniform(lo, hi) for _ in range(n)]
