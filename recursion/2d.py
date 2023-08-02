"""
Дана последовательность целых чисел. Напишите программу с использованием 
рекурсии, которая выводит эту последовательность в обратном порядке.
"""


def main():
    """_summary_

    Returns:
        _type_: _description_
    """
    if (n := int(input())) == 0:
        print(n)
        return None
    main()
    print(n)


if __name__ == "__main__":
    main()
