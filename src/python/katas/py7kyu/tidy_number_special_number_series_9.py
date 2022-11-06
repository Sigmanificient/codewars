"""Kata url: https://www.codewars.com/kata/5a87449ab1710171300000fd."""


def tidy_number(n):
    return (s := str(n)) == ''.join(sorted(s))


def test_tidy_number():
    assert tidy_number(12)
    assert not tidy_number(102)
    assert not tidy_number(9672)
    assert tidy_number(2789)
