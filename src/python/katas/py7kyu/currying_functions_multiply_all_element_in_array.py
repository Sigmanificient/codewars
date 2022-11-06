"""Kata url: https://www.codewars.com/kata/586909e4c66d18dd1800009b."""


def multiply_all(arr):
    def apply(x):
        return [i * x for i in arr]

    return apply


def test_multiply_all():
    assert multiply_all([1, 2, 3])(1) == [1, 2, 3]
    assert multiply_all([1, 2, 3])(2) == [2, 4, 6]
    assert multiply_all([1, 2, 3])(0) == [0, 0, 0]
    assert multiply_all([])(10) == []
