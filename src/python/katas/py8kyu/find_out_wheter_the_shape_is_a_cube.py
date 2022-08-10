"""Kata url: https://www.codewars.com/kata/58d248c7012397a81800005c."""


def cube_checker(volume, side):
    return side > 0 and side ** 3 == volume


def test_cube_checker():
    assert not cube_checker(-12, 2)
    assert not cube_checker(8, 3)
    assert cube_checker(8, 2)

    assert not cube_checker(-8, -2)
    assert cube_checker(27, 3)
    assert not cube_checker(1, 5)
    assert cube_checker(125, 5)
    assert not cube_checker(125, -5)

    assert not cube_checker(0, 0)
    assert not cube_checker(0, 12)
    assert not cube_checker(12, -1)
    assert cube_checker(1, 1)
