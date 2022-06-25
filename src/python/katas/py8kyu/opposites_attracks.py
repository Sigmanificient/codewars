"""Kata url: https://www.codewars.com/kata/555086d53eac039a2a000083."""


def lovefunc(flower1: int, flower2: int) -> bool:
    return bool(flower1 % 2 - flower2 % 2)


def test_lovefunc():
    assert lovefunc(1, 4)
    assert not lovefunc(2, 2)
    assert lovefunc(0, 1)
    assert not lovefunc(0, 0)
