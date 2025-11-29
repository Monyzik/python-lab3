import time


def timeit_once(func, *args, **kwargs) -> float:
    """
    Считает время выполнения func, запущенной один раз.
    :param func: Функция, время которой засекается.
    :param args: Неименованные аргументы функции.
    :param kwargs: Именованные аргументы функции.
    :return: Возвращает время работы func.
    """
    start = time.perf_counter()
    func(*args, **kwargs)
    end = time.perf_counter()
    return end - start
