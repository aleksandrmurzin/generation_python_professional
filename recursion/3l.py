"""
Выберем натуральное число n=16n=16 и будем вычитать из него число 55, пока оно
не перестанет быть положительным:
"""


def main(n):
    """_summary_

    Args:
        n (_type_): _description_
    """
    def rec(n):
        if n > 0:
            print(n)
            rec(n-5)
        print(n)
    return rec(n)


if __name__ == "__main__":
    number = int(input())
    main(number)
