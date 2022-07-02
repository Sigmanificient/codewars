"""Kata url: https://www.codewars.com/kata/5aba780a6a176b029800041c."""


def max_multiple(divisor: int, bound: int) -> int:
    return bound - (bound % divisor)


def test_max_multiple():
    assert max_multiple(2, 7) == 6
    assert max_multiple(3, 10) == 9
    assert max_multiple(7, 17) == 14
    assert max_multiple(10, 50) == 50
    assert max_multiple(37, 200) == 185
    assert max_multiple(7, 100) == 98
