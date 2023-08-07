"""
Реализуйте функцию to_binary() с использованием рекурсии,
которая принимает один аргумент:
"""


def to_binary(n):
    b = ''

    def rec(n, b):
        if n < 1:
            if b == "":
                return "0"
            return b
        b = str(n % 2) + b
        n = n // 2

        return rec(n, b)
    return rec(n, b)


if __name__ == "__main__":
    number = int(input())
    print(to_binary(n=number))
