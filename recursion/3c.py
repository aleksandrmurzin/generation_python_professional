"""
В первый год в пруду живет 7777 лягушек. Каждый год из пруда вылавливают 3030
лягушек, а оставшиеся размножаются, и их становится в три раза больше.
"""


def number_of_frogs(year):
    """_summary_

    Args:
        year (_type_): _description_
    """
    def rec(year, frogs=77):
        if year == 1:
            return frogs
        return rec(year-1, 3*(frogs-30))
    return rec(year)


if __name__ == "__main__":
    y = int(input())
    print(number_of_frogs(y))
