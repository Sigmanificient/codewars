"""Kata url: https://www.codewars.com/kata/55f73be6e12baaa5900000d4."""


def goals(la_liga: int, copa_del_rey: int, champions_league: int) -> int:
    return la_liga + copa_del_rey + champions_league


def test_goals():
    assert goals(0, 0, 0) == 0
    assert goals(5, 10, 2) == 17
    assert goals(1, 2, 3) == 6

    assert goals(10, 0, 0) == 10
    assert goals(0, 10, 0) == 10
    assert goals(0, 0, 10) == 10
