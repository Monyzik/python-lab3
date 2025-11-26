import pytest
from src.algorithms.factorial import factorial_recursive, factorial
from src.exceptions import NegativeNumberException


@pytest.mark.parametrize("n, expected", [(0, 1), (1, 1), (2, 2),
                                         (3, 6), (4, 24), (5, 120),
                                         (10, 3628800)])
def test_factorial(n, expected):
    assert factorial(n) == expected
    assert factorial_recursive(n) == expected


def test_factorial_negative():
    with pytest.raises(NegativeNumberException):
        factorial_recursive(-1)
    with pytest.raises(NegativeNumberException):
        factorial(-1)
