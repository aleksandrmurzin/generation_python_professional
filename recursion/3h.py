def is_power(number):
    def rec(number):
        if number == 1:
            return True
        elif number % 2 == 1:
            return False
        elif number // 2 == 1:
            return True
        number /= 2
        return rec(number)
    return rec(number)


if __name__ == "__main__":
    n = int(input())
    print(is_power(number=n))
