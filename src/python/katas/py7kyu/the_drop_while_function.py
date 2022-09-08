"""Kata url: https://www.codewars.com/kata/54f9c37106098647f400080a."""


def drop_while(arr, pred):
    len_arr = len(arr)

    i = 0
    while i < len_arr and pred(arr[i]):
        i += 1

    return arr[i:]


def test_drop_while():
    def is_even(i):
        return not i % 2

    def is_odd(i):
        return bool(i % 2)

    assert drop_while([2, 6, 4, 10, 1, 5, 4, 3], is_even) == [1, 5, 4, 3]
    assert drop_while([2, 4, 10, 100, 64, 78, 92], is_even) == []
    assert drop_while([1, 2, 3, 4, 5], is_odd) == [2, 3, 4, 5]
    assert drop_while([-1, -5, 127, 86, 902, 2, 1], is_odd) == [86, 902, 2, 1]
    assert drop_while([1, 3, 5, 7, 9, 111], is_odd) == []

    assert drop_while(
        [2, 100, 1000, 10000, 10000, 5, 3, 4, 6], is_even
    ) == [5, 3, 4, 6]

    assert drop_while(
        [998, 996, 12, -1000, 200, 0, 1, 1, 1], is_even
    ) == [1, 1, 1]

    assert drop_while(
        [1, 4, 2, 3, 5, 4, 5, 6, 7], is_even
    ) == [1, 4, 2, 3, 5, 4, 5, 6, 7]

    assert drop_while(
        [1, 5, 111, 1111, 1111, 2, 4, 6, 4, 5], is_odd
    ) == [2, 4, 6, 4, 5]

    assert drop_while(
        [2, 1, 2, 4, 3, 5, 4, 6, 7, 8, 9, 0], is_odd
    ) == [2, 1, 2, 4, 3, 5, 4, 6, 7, 8, 9, 0]
