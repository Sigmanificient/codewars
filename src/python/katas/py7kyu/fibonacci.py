"""Kara url: https://www.codewars.com/kata/57a1d5ef7cb1f3db590002af."""


def fibonacci(n: int) -> int:
    a, b = 0, 1
    for _ in range(abs(n)):
        a, b = b, a + b

    return a


def test_fib():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(34) == 5702887
    assert fibonacci(299) == 137347080577163115432025771710279131845700275212767467264610201
