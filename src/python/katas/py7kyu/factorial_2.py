"""Kata url: https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc."""


def factorial(n: int) -> int:
    if not (0 <= n <= 12):
        raise ValueError

    return n * factorial(n - 1) if n else 1


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
