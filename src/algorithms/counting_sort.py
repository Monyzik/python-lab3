def counting_sort(a: list[int]) -> list[int]:
    """
    Сортировка подсчетом (O(k * n))
    :param a: массив целых чисел, который необходимо отсортировать
    :return: возвращает отсортированный по возрастанию массив
    """
    minimum, maximum = min(a), max(a)
    d = maximum - minimum + 1
    counter = [0] * d
    result = []
    for x in a:
        counter[x - minimum] += 1
    for i in range(0, d):
        for j in range(counter[i]):
            result.append(i + minimum)
    return result
