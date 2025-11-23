from typing import Callable


class EmptyException(Exception):
    def __init__(self, func: Callable, cls):
        super().__init__(f"Невозможно применить функцию {func.__name__} в пустом {cls.__name__}")
