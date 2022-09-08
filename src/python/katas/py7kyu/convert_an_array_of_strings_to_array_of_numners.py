"""Kata url: https://www.codewars.com/kata/5783d8f3202c0e486c001d23."""


def to_float_array(arr):
    return list(map(float, arr))


def test_to_float_array():
    assert to_float_array(["1.1", "2.2", "3.3"]) == [1.1, 2.2, 3.3]
