def recursive_sum(a, b):
    if b == 0:
        return a
    a, b = a + b, b - b
    return recursive_sum(a, b)


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(recursive_sum(a=a, b=b))
