"""Kata url: https://www.codewars.com/kata/568dcc3c7f12767a62000038."""


def set_alarm(employed: bool, vacation: bool) -> bool:
    return employed and not vacation


def test_set_alarm():
    assert not set_alarm(True, True)
    assert not set_alarm(False, True)
    assert not set_alarm(False, False)
    assert set_alarm(True, False)
