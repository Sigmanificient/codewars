"""Kata url: https://www.codewars.com/kata/59c3e8c9f5d5e40cab000ca6."""


def sum_arrays(array1, array2):
    if not array1 and not array2:
        return []

    a = int(''.join(map(str, array1)) or '0')
    b = int(''.join(map(str, array2)) or '0')

    s = a + b
    out = list(map(int, str(abs(s)) or '0'))

    if s < 0:
        out[0] *= -1

    return out


def test_sum_arrays():
    assert sum_arrays([3, 2, 9], [1, 2]) == [3, 4, 1]
    assert sum_arrays([4, 7, 3], [1, 2, 3]) == [5, 9, 6]
    assert sum_arrays([1], [5, 7, 6]) == [5, 7, 7]
    assert sum_arrays([-3, 4, 2], [3, 4, 4]) == [2]
    assert sum_arrays([], []) == []
    assert sum_arrays([0], []) == [0]
    assert sum_arrays([], [1, 2]) == [1, 2]
