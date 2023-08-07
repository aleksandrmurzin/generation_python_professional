"""
Реализуйте функцию is_palindrome() с использованием рекурсии,
которая принимает один аргумент:
"""


def is_palindrome(word):
    """_summary_

    Args:
        word (_type_): _description_

    Returns:
        _type_: _description_
    """
    if len(word) <= 1:
        return True
    elif word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])


if __name__ == "__main__":
    w = input()
    print(is_palindrome(word=w))
