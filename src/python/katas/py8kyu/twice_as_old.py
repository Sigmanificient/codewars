"""Kata url: https://www.codewars.com/kata/5b853229cfde412a470000d0."""


def twice_as_old(dad_years_old: int, son_years_old: int) -> int:
    return abs(dad_years_old - (2 * son_years_old))


def test_twice_as_old():
    assert twice_as_old(36, 7) == 22
    assert twice_as_old(55, 30) == 5
    assert twice_as_old(42, 21) == 0
    assert twice_as_old(22, 1) == 20
    assert twice_as_old(29, 0) == 29
