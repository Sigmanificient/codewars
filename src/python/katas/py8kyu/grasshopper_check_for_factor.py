"""Kata url: https://www.codewars.com/kata/55cbc3586671f6aa070000fb."""


def check_for_factor(base: int, factor: int) -> bool:
    return not base % factor


def test_check_for_factor():
    assert check_for_factor(10, 2)
    assert check_for_factor(63, 7)
    assert check_for_factor(2450, 5)
    assert check_for_factor(24612, 3)

    assert not check_for_factor(9, 2)
    assert not check_for_factor(653, 7)
    assert not check_for_factor(2453, 5)
    assert not check_for_factor(24617, 3)
