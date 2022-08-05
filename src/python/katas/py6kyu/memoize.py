"""Kata url: https://www.codewars.com/kata/59ffef8246d8434b0700001d."""
from typing import Callable, Dict


def memoize(func: Callable[[int], int]) -> Callable[[int], int]:
    cache: Dict[int, int] = {}

    def inner(k: int) -> int:
        if k in cache:
            return cache[k]

        r = func(k)
        cache[k] = r
        return r

    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner


def test_memoize():
    from time import perf_counter, sleep

    @memoize
    def fib(n):
        """Computes the nth number in the Fibonacci sequence"""
        sleep(0.001)
        return fib(n - 2) + fib(n - 1) if n > 1 else [0, 1][n]

    assert fib.__name__ == "fib"
    assert fib.__doc__ == "Computes the nth number in the Fibonacci sequence"

    fib_100 = 354224848179261915075

    assert fib(100) == fib_100

    marker = perf_counter()
    assert fib(100) == fib_100
    assert perf_counter() - marker < 0.05

    __pre_computed = [
        66012, 121415, 223317, 410744, 755476, 1389537, 2555757,
        4700770, 8646064, 15902591, 29249425, 53798080, 98950096,
        181997601, 334745777, 615693474, 1132436852, 2082876103,
        3831006429, 7046319384, 12960201916,
    ]

    @memoize
    def fab(n):
        return fab(n - 3) + fab(n - 2) + fab(n - 1) if n > 2 else [0, 1, 1][n]

    marker = perf_counter()

    for x in range(20, 41):
        # 0.001 * sum(range(20, 41)) => > 0.5 seconds
        assert fab(x) == __pre_computed[x - 20]

    assert perf_counter() - marker < 0.05
