"""Kata url: https://www.codewars.com/kata/5becace7063291bebf0001d5."""


def positive_to_negative(binary):
    if sum(binary) == 0:
        return [0] * len(binary)
    p = 2 ** len(binary)
    k = int(''.join(map(str, binary)), 2)
    return list(map(int, f'{p - k:b}'))


def test_positive_to_negative():
    assert positive_to_negative([0, 1, 0, 0, 1]) == [1, 0, 1, 1, 1]
    assert positive_to_negative([0, 0, 0, 0]) == [0, 0, 0, 0]
    assert positive_to_negative([0, 0, 1, 0]) == [1, 1, 1, 0]
    assert positive_to_negative([0, 0, 1, 1]) == [1, 1, 0, 1]
    assert positive_to_negative([0, 1, 0, 0]) == [1, 1, 0, 0]
    assert positive_to_negative([0, 1, 0, 0]) == [1, 1, 0, 0]
