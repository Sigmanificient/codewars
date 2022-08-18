"""Kata url: https://www.codewars.com/kata/58fa273ca6d84c158e000052."""


def digits(n: int) -> int:
    return len(str(n))


def test_digits():
    assert digits(5) == 1
    assert digits(12345) == 5
    assert digits(9876543210) == 10
