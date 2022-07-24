"""Kata url: https://www.codewars.com/kata/55dc4520094bbaf50e0000cb."""


def am_i_wilson(n: int) -> bool:
    return n in {5, 13, 563}


def test_am_i_wilson():
    assert am_i_wilson(0)
    assert am_i_wilson(5)
    assert am_i_wilson(6)
    assert am_i_wilson(7)
    assert am_i_wilson(13)
    assert am_i_wilson(567)
