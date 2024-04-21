"""Kata url: https://www.codewars.com/kata/5519e930cd82ff8a9a000216."""


def hamming_weight(x: int) -> int:
    return f'{x:b}'.count('1')


def test_hamming_weight():
    assert hamming_weight(0) == 0
    assert hamming_weight(1) == 1
    assert hamming_weight(2) == 1
    assert hamming_weight(10) == 2
    assert hamming_weight(21) == 3
    assert hamming_weight(2048) == 1