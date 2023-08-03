"""
Напишите программу с использованием рекурсивной функции,
которая выводит изображение песочных часов,
составленное из цифр 11, 22, 33, и 44:
"""


def main():
    """_summary_
    """
    def rec(n):
        k = 16 - 4 * (n - 1)
        if k >= 8 and n <= 16:
            line = str(n) * k
            line = line.center(16)
            print(line)
            rec(n+1)
        line = str(n) * k
        line = line.center(16)
        print(line)
    rec(1)


if __name__ == "__main__":
    main()
