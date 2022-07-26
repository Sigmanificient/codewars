"""Kata url: https://www.codewars.com/kata/567bf4f7ee34510f69000032."""
import re


def is_digit(n):
    return bool(re.fullmatch(r"(\d)", n))


def test_is_digit():
    assert not is_digit("")
    assert not is_digit(" ")
    assert not is_digit("a")
    assert not is_digit("a5")
    assert is_digit("7")
