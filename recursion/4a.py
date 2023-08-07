"""
Функция должна вычислять сумму всех чисел во всех списках и возвращать
полученный результат. Если список nested_lists пуст, функция должна вернуть
число 0.
"""


def recursive_sum(numbers):
    """_summary_

    Args:
        numbers (_type_): _description_

    Returns:
        _type_: _description_
    """
    rec_sum = 0

    def rec(n):
        nonlocal rec_sum
        for i in n:
            if isinstance(i, int):
                rec_sum += i
            else:
                rec(n=i)
    rec(n=numbers)
    return rec_sum


if __name__ == "__main__":
    my_list = [1, [4, 4], 2, [1, [2, 10]]]
    print(recursive_sum(numbers=my_list))
