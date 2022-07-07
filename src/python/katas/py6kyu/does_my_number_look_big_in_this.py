"""Kata url: https://www.codewars.com/kata/5287e858c6b5a9678200083c."""


def narcissistic(value: int) -> bool:
    _str_val = str(value)
    _len = len(_str_val)
    return sum(int(d) ** _len for d in _str_val) == value


def test_narcissistic():
    assert narcissistic(0)
    assert narcissistic(7)
    assert narcissistic(371)
    assert not narcissistic(122)
    assert not narcissistic(4887)
