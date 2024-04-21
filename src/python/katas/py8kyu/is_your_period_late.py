"""Kata url: https://www.codewars.com/kata/578a8a01e9fd1549e50001f1."""

from datetime import date


def period_is_late(last: date, today: date, cycle_length: int) -> int:
    return (today - last).days > cycle_length


def test_period_is_late():
    assert not period_is_late(date(2016, 6, 13), date(2016, 7, 16), 35)
    assert period_is_late(date(2016, 6, 13), date(2016, 7, 16), 28)
    assert not period_is_late(date(2016, 6, 13), date(2016, 7, 16), 35)
    assert not period_is_late(date(2016, 6, 13), date(2016, 6, 29), 28)
    assert not period_is_late(date(2016, 7, 12), date(2016, 8, 9), 28)
    assert period_is_late(date(2016, 7, 12), date(2016, 8, 10), 28)
    assert period_is_late(date(2016, 7, 1), date(2016, 8, 1), 30)
    assert not period_is_late(date(2016, 6, 1), date(2016, 6, 30), 30)
    assert not period_is_late(date(2016, 1, 1), date(2016, 1, 31), 30)
    assert period_is_late(date(2016, 1, 1), date(2016, 2, 1), 30)