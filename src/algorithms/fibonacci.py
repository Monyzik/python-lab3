from functools import lru_cache

from src.exceptions import NegativeNumberException


def matrix_multiply(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    """
    Вычисление произведение двух матриц
    :param a: матрица 1 (m x n)
    :param b: матрица 2 (n x k)
    :return: матрица, которая является произведением двух матриц (m x k)
    """
    if not a or not b or len(a[0]) != len(b):
        raise ValueError
    ans = [[0 for _ in range(len(b[0]))] for __ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                ans[i][j] += a[i][k] * b[k][j]
    return ans


def matrix_binary_pow(a: list[list[int]], n: int) -> list[list[int]]:
    """
    Бинарное возведение матрицы в степень (работает за O(k * log(n)),
    где k - сложность вычисления произведения матриц)
    :param a: Матрица (n x n)
    :param n: Степень в которую возводится матрица.
    :return: Матрица a возведенная в степень n
    """
    if n <= 0:
        raise NegativeNumberException(matrix_multiply)
    if n == 1:
        return a
    if n % 2:
        return matrix_multiply(a, matrix_binary_pow(a, n - 1))
    x = matrix_binary_pow(a, n // 2)
    return matrix_multiply(x, x)


def fibo(n: int) -> int:
    """
    Вычисление числа Фибоначчи с помощью бинарного возведения в степень матрицы [[1, 1], [1, 0]]
    Временная сложность O(log(n))
    :param n: Номер числа Фибоначчи
    :return: Число Фибоначчи
    """
    if n < 0:
        raise NegativeNumberException(fibo)
    if n == 0:
        return 0
    return matrix_binary_pow([[1, 1], [1, 0]], n)[0][1]


@lru_cache(maxsize=None)
def fibo_recursive(n: int) -> int:
    """
    Вычисление числа Фибоначчи с помощью рекурсии
    Временная сложность O(n) из-за кэширования
    :param n: Номер числа Фибоначчи
    :return: Число Фибоначчи
    """
    if n < 0:
        raise NegativeNumberException(fibo_recursive)
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)
