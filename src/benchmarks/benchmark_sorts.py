import copy
from typing import Callable

from src.benchmarks.timeit_once import timeit_once


def benchmark_sorts(arrays: dict[str, list], algos: dict[str, Callable]) -> dict[str, dict[str, float]]:
    results = {}
    for array_name, array in arrays.items():
        results[array_name] = {}
        for algo_name, algo_func in algos.items():
            try:
                execution_time = timeit_once(algo_func, copy.deepcopy(array))
                results[array_name][algo_name] = execution_time
            except Exception as exception:
                results[array_name][algo_name] = -1
                print(f"Ошибка при работе алгоритма {algo_name} на массиве {array_name}: {exception}")
    return results
