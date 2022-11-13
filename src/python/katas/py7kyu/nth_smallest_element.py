"""Kata url: https://www.codewars.com/kata/5a512f6a80eba857280000fc."""


def nth_smallest(arr, pos):
    return sorted(arr)[pos - 1]


def test_nth_smallest():
    assert nth_smallest([3, 1, 2], 2) == 2
    assert nth_smallest([15, 20, 7, 10, 4, 3], 3) == 7
    assert nth_smallest([-5, -1, -6, -18], 4) == -1
    assert nth_smallest([-102, -16, -1, -2, -367, -9], 5) == -2
    assert nth_smallest([2, 169, 13, -5, 0, -1], 4) == 2
