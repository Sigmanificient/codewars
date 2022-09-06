"""Kata url: https://www.codewars.com/kata/566fc12495810954b1000030."""


def nb_dig(n, d):
    sd = str(d)
    return sum(str(i ** 2).count(sd) for i in range(n + 1))


def test_nb_dig():
    assert nb_dig(5750, 0) == 4700
    assert nb_dig(11011, 2) == 9481
    assert nb_dig(12224, 8) == 7733
    assert nb_dig(11549, 1) == 11905
