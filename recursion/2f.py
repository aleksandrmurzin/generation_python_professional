def triangle(h):
    """_summary_

    Args:
        h (_type_): _description_

    Returns:
        _type_: _description_
    """
    def rec(r):
        if r <= h: 
            print("*" * r)
            rec(r+1)
        return None
    rec(1)
    return None


if __name__ == "__main__":
    h = int(input())
    triangle(h)
