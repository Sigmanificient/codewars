"""Kata url: https://www.codewars.com/kata/59a1cdde9f922b83ee00003b."""


def stanton_measure(arr):
    return arr.count(arr.count(1))


def test_stanton_measure():
    assert stanton_measure([1, 4, 3, 2, 1, 2, 3, 2]) == 3
