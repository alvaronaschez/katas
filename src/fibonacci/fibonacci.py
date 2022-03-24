from functools import cache


@cache
def recursive_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("math domain error")

    return n if n <= 1 else recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


def iterative_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("math domain error")

    i, j = 0, 1
    for _ in range(n):
        i, j = j, i + j
    return i


def generator_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("math domain error")

    def fib_gen():
        i, j = 0, 1
        while True:
            yield i
            i, j = j, i + j

    result: int
    fibonacci_sequence = fib_gen()
    for _ in range(n + 1):
        result = next(fibonacci_sequence)
    return result
