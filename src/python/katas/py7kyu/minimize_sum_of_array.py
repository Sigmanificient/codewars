"""Kata url: https://www.codewars.com/kata/5a523566b3bfa84c2e00010b."""


def min_sum(arr):
    half = len(arr) // 2
    arr = sorted(arr)

    return sum(x * y for x, y in zip(arr[:half], arr[half:][::-1]))


def test_min_sum():
    assert min_sum([5, 4, 2, 3]) == 22
    assert min_sum([12, 6, 10, 26, 3, 24]) == 342
    assert min_sum([9, 2, 8, 7, 5, 4, 0, 6]) == 74
