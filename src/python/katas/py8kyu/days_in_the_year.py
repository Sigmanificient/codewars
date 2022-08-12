"""Kata url: https://www.codewars.com/kata/56d6c333c9ae3fc32800070f."""


def year_days(year: int) -> str:
    days = 365 + (not year % 4) - (not year % 100) + (not year % 400)
    return f'{year} has {days} days'


def test_year_days():
    assert year_days(0)
    assert year_days(-64)
    assert year_days(2016)
    assert year_days(1974)
    assert year_days(-10)
    assert year_days(666)
    assert year_days(1857)
    assert year_days(2000)
    assert year_days(-300)
    assert year_days(-1)
