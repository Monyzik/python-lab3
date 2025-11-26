import random


def many_duplicates(n: int, k_unique=5, *, seed=None) -> list[int]:
    if seed is not None:
        random.seed(seed)
    a = list(range(k_unique))
    return [random.choice(a) for _ in range(n)]
