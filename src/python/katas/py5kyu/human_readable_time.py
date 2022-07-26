"""Kata url: https://www.codewars.com/kata/52685f7382004e774f0001f7."""


def make_readable(seconds: int) -> str:
    r, s = divmod(seconds, 60)
    h, m = divmod(r, 60)
    return f"{h:02}:{m:02}:{s:02}"


def test_make_readable():
    assert make_readable(0) == "00:00:00"
    assert make_readable(5) == "00:00:05"
    assert make_readable(60) == "00:01:00"
    assert make_readable(86399) == "23:59:59"
    assert make_readable(359999) == "99:59:59"
