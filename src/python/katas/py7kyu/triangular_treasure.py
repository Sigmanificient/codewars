"""Kata url: https://www.codewars.com/kata/525e5a1cb735154b320002c8."""


def triangular(n: int) -> int:
    if n < 0:
        return 0

    x = ((n + 1) // 2) * n
    if not n % 2:
        x += n // 2

    return x


def test_triangle():
    assert triangular(2) == 3
    assert triangular(7) == 28
    assert triangular(12) == 78
    assert triangular(25) == 325
    assert triangular(50) == 1275
    assert triangular(1000) == 500500
    assert triangular(5000) == 12502500
    assert triangular(10000) == 50005000
    assert triangular(0) == 0
    assert triangular(-1) == 0
    assert triangular(-5) == 0
