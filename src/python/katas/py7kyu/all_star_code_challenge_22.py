"""Kata url: https://www.codewars.com/kata/5865cff66b5699883f0001aa."""


def to_time(seconds):
    r, _ = divmod(seconds, 60)
    h, m = divmod(r, 60)
    return f"{h} hour(s) and {m} minute(s)"


def test_to_time():
    assert to_time(3600) == '1 hour(s) and 0 minute(s)'
    assert to_time(3601) == '1 hour(s) and 0 minute(s)'
    assert to_time(3500) == '0 hour(s) and 58 minute(s)'
    assert to_time(323500) == '89 hour(s) and 51 minute(s)'
    assert to_time(0) == '0 hour(s) and 0 minute(s)'
