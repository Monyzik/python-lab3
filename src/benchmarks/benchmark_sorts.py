import copy
from typing import Callable

from src.benchmarks.timeit_once import timeit_once


def benchmark_sorts(arrays: dict[str, list], algos: dict[str, Callable]) -> dict[str, dict[str, float]]:
    """
    Замеряет время работы сортировок на заданных массивах
    :param arrays: Кортеж массивов для бенчмарка.
    :param algos: Кортеж алгоритмов сортировки.
    :return: Возвращает кортеж, где первый ключ алгоритм, а второй массив
    """
    results = {}
    for algo_name, algo_func in algos.items():
        results[algo_name] = {}
        for array_name, array in arrays.items():
            try:
                execution_time = timeit_once(algo_func, copy.deepcopy(array))
                results[algo_name][array_name] = execution_time
            except Exception as exception:
                results[algo_name][array_name] = -1
                print(f"Ошибка при работе алгоритма {algo_name} на массиве {array_name}: {exception}")
    return results
