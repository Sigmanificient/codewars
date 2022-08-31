"""Kata url: https://www.codewars.com/kata/581e1d083a4820eb4f00004f."""


def mod256_without_mod(n):
    while n >= 256:
        n -= 256

    while n < 0:
        n += 256

    return n


def test_mod256_without_mod():
    assert mod256_without_mod(254) == 254
    assert mod256_without_mod(256) == 0
    assert mod256_without_mod(258) == 2
    assert mod256_without_mod(-254) == 2
    assert mod256_without_mod(-256) == 0
    assert mod256_without_mod(-258) == 254
