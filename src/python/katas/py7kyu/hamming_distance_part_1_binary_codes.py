"""Kata url: https://www.codewars.com/kata/5624e574ec6034c3a20000e6."""


def hamming_distance(a, b):
    return sum(x != y for x, y in zip(a, b))


def test_hamming_distance():
    assert hamming_distance('100101', '101001') == 2
    assert hamming_distance('1010', '0101') == 4
    assert hamming_distance(
        '100101011011010010010', '101100010110010110101'
    ) == 9
