"""Kata url: https://www.codewars.com/kata/588a3c3ef0fbc9c8e1000095."""


def max_diff(lst):
    return max(lst, default=0) - min(lst, default=0)


def test_max_diff():
    assert max_diff([0, 1, 2, 3, 4, 5, 6]) == 6
    assert max_diff([-0, 1, 2, -3, 4, 5, -6]) == 11
    assert max_diff([0, 1, 2, 3, 4, 5, 16]) == 16
    assert max_diff([16]) == 0
    assert max_diff([]) == 0
