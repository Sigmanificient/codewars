"""Kata url: https://www.codewars.com/kata/55b051fac50a3292a9000025."""


def filter_string(string: str) -> int:
    return int(''.join(filter(str.isdigit, string)))


def test_filter_string():
    assert filter_string("123") == 123
    assert filter_string("a1b2c3") == 123
    assert filter_string("aa1bb2cc3dd") == 123
    assert filter_string("aa 112 3dd") == 1123
    assert filter_string("11bb2c23c3") == 112233
