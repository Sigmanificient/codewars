"""Kata url: https://www.codewars.com/kata/636f26f52aae8fcf3fa35819."""
import sys

total_bytes = sys.getsizeof


def test_total_bytes():
    assert total_bytes("hello") == 54
    assert total_bytes(123) == 28
    assert total_bytes([":)", 1]) == 72
    assert total_bytes({'john': 19}) == 232
