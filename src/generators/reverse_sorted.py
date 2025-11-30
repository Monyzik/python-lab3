from src.exceptions import NegativeNumberException


def reverse_sorted(n: int) -> list[int]:
    """
    Генерирует обратно отсортированный массив.
    :param n: Размер массива.
    :return: Возвращает обратно отсортированный массив.
    """
    if n < 0:
        raise NegativeNumberException(reverse_sorted)
    return list(range(n - 1, -1, -1))
