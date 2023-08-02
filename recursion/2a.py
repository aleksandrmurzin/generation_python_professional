"""Вам доступна функция traffic(), реализованная с помощью цикла while,
которая принимает в качестве аргумента число nn и выводит nn раз строку Не парковаться.
"""


def traffic(n):
    if n <= 0:
        return None
    print("Не парковаться")
    return traffic(n=n-1)


if __name__ == "__main__":
    n = int(input())
    traffic(n=n)
