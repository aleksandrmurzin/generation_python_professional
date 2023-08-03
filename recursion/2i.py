def print_digits(number):
    """_summary_

    Args:
        number (_type_): _description_

    Returns:
        _type_: _description_
    """
    number = str(number)

    def rec(i):
        if i >= len(number):
            return None
        print(number[i])
        rec(i+1)
    rec(0)


if __name__ == "__main__":
    n = int(input())
    print_digits(n)
