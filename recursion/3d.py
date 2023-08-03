def range_sum(numbers, start, end):
    """_summary_

    Args:
        numbers (_type_): _description_
        start (_type_): _description_
        end (_type_): _description_
    """
    def rec(numbers, current_sum=0):
        if numbers == []:
            return current_sum
        return rec(numbers[1:], current_sum + numbers[0])
    return rec(numbers[start:end+1])


if __name__ == "__main__":
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    s = 3
    e = 7
    print(range_sum(n, s, e))
