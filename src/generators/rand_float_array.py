import random


def rand_float_array(n: int, lo=0.0, hi=1.0, *, seed=None) -> list[float]:
    if lo > hi:
        raise ValueError(f"Нижняя граница не может быть больше верхней")
    if seed is not None:
        random.seed(seed)

    return [random.uniform(lo, hi) for _ in range(n)]
