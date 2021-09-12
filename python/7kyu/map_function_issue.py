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
