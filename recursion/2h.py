def print_digits(number):
    """_summary_

    Args:
        number (_type_): _description_

    Returns:
        _type_: _description_
    """
    string = str(number)
    if len(string) == 0:
        return None
    print(string[-1])
    if string[:-1] == "":
        return None
    print_digits(int(string[:-1]))


if __name__ == "__main__":
    n = int(input())
    print_digits(n)
