"""Kata url: https://www.codewars.com/kata/563c13853b07a8f17c000022."""
from datetime import datetime


def is_today(date):
    return (
        datetime.today().strftime("%D")
        == date.strftime("%D")
    )


def test_is_today():
    assert not is_today(datetime(2020, 10, 1, 1, 1, 1, 1))
    assert not is_today(datetime(2080, 10, 1, 1, 1, 1, 1))
    assert is_today(datetime.today())
