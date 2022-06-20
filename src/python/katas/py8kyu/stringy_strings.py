"""Kata url: https://www.codewars.com/kata/563b74ddd19a3ad462000054."""


def stringy(size):
    return '10' * (size // 2) + ('1' * (size % 2))


def test_stringy():
    assert type(stringy(5)) == str
    assert stringy(10)[0] == '1'

    for i in range(1, 5):
        assert len(stringy(i)) == i

    assert stringy(3) == '101'
    assert stringy(5) == '10101'
    assert stringy(12) == '101010101010'
    assert stringy(26) == '10101010101010101010101010'
    assert stringy(28) == '1010101010101010101010101010'
