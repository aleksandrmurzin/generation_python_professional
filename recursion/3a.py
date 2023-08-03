"""
Напишите программу с использованием рекурсии, которая принимает на вход число
и выводит количество цифр в этом числе.
"""


def main(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    def rec(number=n, length=0):
        if number == "":
            return length
        length += 1
        return rec(number[1:], length)
    return rec(str(n))


if __name__ == "__main__":
    n = int(input())
    print(main(n))
