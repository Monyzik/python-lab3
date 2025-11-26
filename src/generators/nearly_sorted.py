import random


def nearly_sorted(n: int, swaps: int, *, seed=None) -> list[int]:
    if seed is not None:
        random.seed(seed)
    ans = list(range(n))
    for i in range(swaps):
        i, j = random.sample(ans, 2)
        ans[i], ans[j] = ans[j], ans[i]
    return ans


print(nearly_sorted(5, 5, seed=1))
print(nearly_sorted(5, 5, seed=1))