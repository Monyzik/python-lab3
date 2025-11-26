from typing import Callable


class EmptyException(Exception):
    def __init__(self, func: Callable, cls):
        super().__init__(f"Невозможно применить функцию {func.__name__} в пустом {cls.__name__}")


class NegativeNumberException(Exception):
    def __init__(self, func: Callable):
        super().__init__(f"Невозможно выполнить функцию {func.__name__} с отрицательным аргументом")


class CmpAndKeyTogetherException(Exception):
    def __init__(self, func: Callable):
        super().__init__(f"Невозможно выполнить сортировку {func} по cmp и key одновременно")
