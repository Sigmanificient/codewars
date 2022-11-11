"""Kata url: https://www.codewars.com/kata/526c7363236867513f0005ca."""


def is_leap_year(year):
    return not (year % 4) - (not year % 100) + (not year % 400)


def test_is_leap_year():
    assert is_leap_year(1984)
    assert is_leap_year(2000)
    assert is_leap_year(2004)
    assert is_leap_year(8)

    assert not is_leap_year(1234)
    assert not is_leap_year(1100)
    assert not is_leap_year(1194)
