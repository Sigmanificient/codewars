"""Kata url: https://www.codewars.com/kata/55192f4ecd82ff826900089e."""


def divide(weight: int) -> bool:
    return not weight % 2 and weight != 2


def test_divide():
    assert divide(4)
    assert not divide(2)
    assert not divide(5)
    assert divide(88)
    assert divide(100)
    assert not divide(67)
    assert divide(90)
    assert divide(10)
    assert not divide(99)
    assert divide(32)
