from src.exceptions import NegativeNumberException


def radix_sort(a: list[int], base: int = 10) -> list[int]:
    """
    Поразрядная сортировка (O(k * n))
    :param a: Массив целых чисел, который необходимо отсортировать.
    :param base: Основание системы счисления в которой производится расчет.
    :return: Возвращает отсортированный по возрастанию массив
    """
    if base <= 0:
        raise NegativeNumberException(radix_sort)
    if base == 1:
        raise ValueError("Невозможно выполнить radix_sort по основанию 1")
    maximum = max(a)
    p = 1
    digits_plus, digits_minus = [[] for _ in range(base)], [[] for _ in range(base)]
    while maximum // p > 0:
        for x in a:
            if x >= 0:
                digits_plus[(x // p) % base].append(x)
            else:
                digits_minus[(x // p) % base].append(x)
        a = [x for q in digits_minus for x in q] + [x for q in digits_plus for x in q]
        p *= base
        digits_plus, digits_minus = [[] for _ in range(base)], [[] for _ in range(base)]

    return a

