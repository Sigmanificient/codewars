"""Kata url: https://www.codewars.com/kata/57b68bc7b69bfc8209000307."""


def average(array):
    return round(sum(array) / len(array))


def test_average():
    assert average([5, 78, 52, 900, 1]) == 207
    assert average([5, 25, 50, 75]) == 39
    assert average([2]) == 2
    assert average([1, 1, 1, 1, 9999]) == 2001
    assert average([0]) == 0
