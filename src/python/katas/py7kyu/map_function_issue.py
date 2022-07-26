"""Kata url: https://www.codewars.com/kata/560fbc2d636966b21e00009e."""


def map_(arr, func):
    if not callable(func):
        return "given argument is not a function"

    if not all(isinstance(x, int) or x.isdigit() for x in arr):
        return "array should contain only numbers"

    return [func(item) for item in arr]


def test_map():
    def func(n):
        return not bool(int(n) % 2)

    assert map_([], func) == []
    assert map_([1, 2, 3, "8"], func) == [False, True, False, True]
    assert map_([77, 84, 18, 43, 16, 70, 53], func) == [
        False,
        True,
        True,
        False,
        True,
        True,
        False,
    ]
    assert map_([1, 96, 37, 60, 7], "test") == "given argument is not a function"
    assert map_([72, 12, 30, "q"], func) == "array should contain only numbers"
    assert map_([9, 53], func) == [False, False]
