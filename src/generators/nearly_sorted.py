import random

from src.exceptions import NegativeNumberException


def nearly_sorted(n: int, swaps: int, *, seed=None) -> list[int]:
    """
    Генерирует почти отсортированный массив с swaps перестановками.
    :param n: Размер массива.
    :param swaps: Количество перестановок.
    :param seed: Параметр генерации.
    :return: Возвращает почти отсортированный массив с swaps перестановками.
    """
    if n < 0:
        raise NegativeNumberException(nearly_sorted)
    if seed is not None:
        random.seed(seed)
    ans = list(range(n))
    for i in range(swaps):
        i, j = random.sample(ans, 2)
        ans[i], ans[j] = ans[j], ans[i]
    return ans
