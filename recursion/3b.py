"""
Напишите программу с использованием рекурсии, которая принимает на вход число и 
выводит сумму цифр этого числа.
"""


def main(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    def rec(n=n, s=0):
        if n == "":
            return s
        s += int(n[0])
        return rec(n[1:], s)
    return rec(str(n))


if __name__ == "__main__":
    n = int(input())
    print(main(n))
