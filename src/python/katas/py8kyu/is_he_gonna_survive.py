"""Kata url: https://www.codewars.com/kata/59ca8246d751df55cc00014c."""


def hero(bullets: int, dragons: int) -> bool:
    return bullets >= dragons * 2


def test_hero():
    assert hero(10, 5)
    assert hero(100, 40)
    assert not hero(4, 5)
    assert not hero(7, 4)
    assert not hero(1500, 751)
    assert not hero(0, 1)


