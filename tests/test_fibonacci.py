import pytest
from src.algorithms.fibonacci import fibo_recursive, fibo
from src.exceptions import NegativeNumberException


@pytest.mark.parametrize("n, expected", [(0, 0), (1, 1), (2, 1), (3, 2),
                                         (4, 3), (5, 5), (6, 8), (7, 13),
                                         (100, 354224848179261915075)])
def test_fibonacci(n, expected):
    assert fibo(n) == expected
    assert fibo_recursive(n) == expected

def test_fibonacci_negative():
    with pytest.raises(NegativeNumberException):
        fibo_recursive(-1)
    with pytest.raises(NegativeNumberException):
        fibo(-1)
