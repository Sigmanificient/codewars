"""Kata url: https://www.codewars.com/kata/587c37897f7dc251a0000001."""


def map(f, iterable):
    return [f(i) for i in iterable]


def test_map():
    assert map(sum, [[1, 2, 3], [4, 5], [6, 7, 8]]) == [6, 9, 21]
    assert map(str, [1, 2, 3]) == ['1', '2', '3']
    assert map(int, ['34', '23']) == [34, 23]
    assert map(ord, 'Hello') == [72, 101, 108, 108, 111]
    assert map(chr, [87, 111, 114, 108, 100]) == ['W', 'o', 'r', 'l', 'd']
