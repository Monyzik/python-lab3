from math import isqrt, floor

from src.exceptions import NegativeNumberException


def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]:
    """
    Блочная (карманная) сортировка (O(n * buckets))
    :param a: массив целых чисел, который необходимо отсортировать
    :param buckets: количество "корзинок"
    :return: возвращает отсортированный по возрастанию массив
    """
    if buckets is None:
        buckets = max(2, isqrt(len(a)))
    if buckets <= 0:
        raise NegativeNumberException(bucket_sort)
    if len(a) <= 1:
        return a
    minimum, maximum = min(a), max(a)
    if minimum == maximum:
        return a
    d = maximum - minimum
    b, answer = [[] for _ in range(buckets)], []
    for x in a:
        index = min(buckets - 1, floor((x - minimum) / d * buckets))
        b[index].append(x)
    for i in range(buckets):
        b[i] = bucket_sort(b[i])
    for bucket in b:
        for x in bucket:
            answer.append(x)
    return answer


# print(bucket_sort([10, 10, 10, 4, 5, 6, 7, 8, 7, 1, 10, 11]))
# print(bucket_sort([-10000, -1, 0, 0.1, 0.2, 0.3476751, 0.347675, 1]))
# print(bucket_sort([1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1], buckets=0))
