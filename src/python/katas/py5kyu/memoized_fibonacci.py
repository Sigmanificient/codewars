"""Kata url: https://www.codewars.com/kata/529adbf7533b761c560004e5."""


def memoized(func):
    cache = {}

    def inner(k):
        if x := cache.get(k):
            return x

        r = func(k)
        cache[k] = r
        return r

    return inner


@memoized
def fibonacci(n):
    return n if n in [0, 1] else fibonacci(n - 1) + fibonacci(n - 2)


def test_fibonacci_memoized():
    assert fibonacci(70) == 190392490709135
    assert fibonacci(60) == 1548008755920
    assert fibonacci(50) == 12586269025


def test_memoized():
    from time import sleep, perf_counter

    @memoized
    def _test(k):
        sleep(0.05)
        return k

    t = perf_counter()
    assert [_test(5) for _ in range(10)] == [5] * 10
    assert perf_counter() - t < 0.1