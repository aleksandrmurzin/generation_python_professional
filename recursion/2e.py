def triangle(h):
    """_summary_

    Args:
        h (_type_): _description_

    Returns:
        _type_: _description_
    """
    if h <= 0:
        return None
    print("*" * h)
    triangle(h-1)
    return None


if __name__ == "__main__":
    h = int(input())
    triangle(h)
