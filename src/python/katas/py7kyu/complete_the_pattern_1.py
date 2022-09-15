"""Kata url: https://www.codewars.com/kata/5572f7c346eb58ae9c000047."""


def pattern(n):
    return '\n'.join(f'{x}' * x for x in range(1, n + 1))


def test_pattern():
    assert pattern(1) == "1"
    assert pattern(2) == "1\n22"
    assert pattern(5) == "1\n22\n333\n4444\n55555"
    assert pattern(0) == ""
    assert pattern(-25) == ""
