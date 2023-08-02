"""Напишите программу с использованием рекурсии,
которая выводит последовательность натуральных чисел от 11 до 100100 включительно."""


def main(n=1):
    """_summary_

    Args:
        n (int, optional): _description_. Defaults to 1.

    Returns:
        _type_: _description_
    """
    if n > 100:
        return None
    print(n)
    n += 1
    return main(n)


if __name__ == "__main__":
    main()
