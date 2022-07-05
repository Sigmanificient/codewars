"""Kata url: https://www.codewars.com/kata/560fbc2d636966b21e00009e."""

def func(n):
    return not bool(int(n) % 2)


def map(arr, somefunction):
    if not callable(somefunction):
        return 'given argument is not a function'

    if not all(
            isinstance(x, int) or x.isdigit()
            for x in arr
    ):
        return 'array should contain only numbers'

    return [somefunction(item) for item in arr]


def test_map():
    assert map([], func) == []
    assert map([1, 2, 3, '8'], func) == [False, True, False, True]
    assert map([77, 84, 18, 43, 16, 70, 53], func) == [False, True, True, False, True, True, False]
    assert map([1, 96, 37, 60, 7], 'test') == 'given argument is not a function'
    assert map([72, 12, 30, 'q'], func) == 'array should contain only numbers'
    assert map([9, 53], func) == [False, False]
