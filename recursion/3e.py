def get_pow(a, n):
    """_summary_

    Args:
        a (_type_): _description_
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    if n == 0:
        return 1
    return a * get_pow(a, n-1)


if __name__ == "__main__":
    a = int(input())
    n = int(input())
    print(get_pow(a=a, n=n))
