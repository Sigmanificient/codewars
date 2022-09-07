"""Kata url: https://www.codewars.com/kata/57d2807295497e652b000139."""


def averages(arr):
    if not arr:
        return []

    return [
        (x + y) / 2
        for x, y in zip(arr, arr[1::])
    ]


def test_averages():
    assert averages([2, 2, 2, 2, 2]) == [2, 2, 2, 2]
    assert averages([2, -2, 2, -2, 2]) == [0, 0, 0, 0]
    assert averages([1, 3, 5, 1, -10]) == [2, 4, 3, -4.5]
    assert averages([]) == []
