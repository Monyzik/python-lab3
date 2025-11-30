import random

from src.exceptions import NegativeNumberException


def many_duplicates(n: int, k_unique=5, *, seed=None) -> list[int]:
    """
    Генерирует массив размера n с k_unique уникальными значениями.
    :param n: Размер массива.
    :param k_unique: Количество уникальных значений.
    :param seed: Параметр генерации.
    :return: Возвращает массив размера n с k_unique уникальными значениями.
    """
    if n < 0:
        raise NegativeNumberException(many_duplicates)
    if seed is not None:
        random.seed(seed)
    a = list(range(k_unique))
    return [random.choice(a) for _ in range(n)]
