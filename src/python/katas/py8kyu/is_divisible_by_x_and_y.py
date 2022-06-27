"""Kata url: https://www.codewars.com/kata/5545f109004975ea66000086."""


def is_divisible(n: int, x: int, y: int) -> bool:
    return (n / x).is_integer() and (n / y).is_integer()


def test_is_divisible():
    assert is_divisible(12, 3, 4)
    assert not is_divisible(3, 2, 2)
    assert not is_divisible(3, 3, 4)
    assert not is_divisible(8, 3, 4)
