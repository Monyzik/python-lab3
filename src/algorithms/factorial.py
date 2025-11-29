from src.exceptions import NegativeNumberException


def factorial(n: int) -> int:
    """
    Итеративное вычисление факториала (O(n))
    :param n: значение факториала
    :return: n!
    """
    if n < 0:
        raise NegativeNumberException(factorial)
    if n == 0:
        return 1
    ans = 1
    for i in range(1, n + 1):
        ans = ans * i
    return ans


def factorial_recursive(n: int) -> int:
    """
    Рекурсивное вычисление факториала (O(n))
    :param n: значение факториала
    :return: n!
    """
    if n < 0:
        raise NegativeNumberException(factorial_recursive)
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)
