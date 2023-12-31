from functools import lru_cache


@lru_cache
def tribonacci(n):
    if n <= 3:
        return 1
    return tribonacci(n-3) + tribonacci(n-2) + tribonacci(n-1)


if __name__ == "__main__":
    number = int(input())
    print(tribonacci(number))
