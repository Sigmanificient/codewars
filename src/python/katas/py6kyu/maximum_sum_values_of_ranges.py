"""Kata url: https://www.codewars.com/kata/583d10c03f02f41462000137."""


def max_sum(arr, ranges):
    return max(sum(arr[x:y + 1]) for x, y in ranges)


def test_max_sum():
    assert max_sum(
        [1, -2, 3, 4, -5, -4, 3, 2, 1],
        [[1, 3], [0, 4], [6, 8]]
    ) == 6
    assert max_sum([1, -2, 3, 4, -5, -4, 3, 2, 1], [[1, 3]]) == 5
    assert max_sum(
        [1, -2, 3, 4, -5, -4, 3, 2, 1],
        [[1, 4], [2, 5]]
    ) == 0
    assert max_sum(
        [11, -22, 31, 34, -45, -46, 35, 32, 21],
        [[1, 4], [0, 3], [6, 8], [0, 8]]
    ) == 88
