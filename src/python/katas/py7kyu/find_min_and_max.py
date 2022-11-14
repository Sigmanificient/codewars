"""Kata url: https://www.codewars.com/kata/57a1ae8c7cb1f31e4e000130."""


def get_min_max(seq):
    return min(seq), max(seq)


def test_get_min_max():
    assert get_min_max([1]), (1, 1)
    assert get_min_max([1, 2]), (1, 2)
    assert get_min_max([2, 1]), (1, 2)
