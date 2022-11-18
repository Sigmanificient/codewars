"""Kata url: https://www.codewars.com/kata/56d93f249c844788bc000002."""


def _testit(s):
    return ' '.join(w[::-1].capitalize()[::-1] for w in s.split(' '))


def test_testit():
    assert _testit("") == ""
    assert _testit("a") == "A"
    assert _testit("b") == "B"
    assert _testit("a a") == "A A"
    assert _testit("a b") == "A B"
    assert _testit("a b c") == "A B C"
