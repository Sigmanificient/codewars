"""Kata url: https://www.codewars.com/kata/5a2b703dc5e2845c0900005a."""


def is_divide_by(number: int, a: int, b: int) -> bool:
    return (number / a).is_integer() and (number / b).is_integer()


def test_is_divisible_by():
    assert is_divide_by(8, 2, 4)
    assert is_divide_by(12, -3, 4)
    assert not is_divide_by(8, 3, 4)
    assert not is_divide_by(48, 2, -5)
    assert is_divide_by(-100, -25, 10)
    assert not is_divide_by(10000, 5, -3)
    assert is_divide_by(4, 4, 2)
    assert not is_divide_by(5, 2, 3)
    assert not is_divide_by(-96, 25, 17)
    assert is_divide_by(33, 1, 33)
