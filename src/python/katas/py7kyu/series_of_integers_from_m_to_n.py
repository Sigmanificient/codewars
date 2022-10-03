"""Kata url: https://www.codewars.com/kata/5841f680c5c9b092950001ae."""


def generate_integers(m, n):
    return list(range(m, n + 1))


def test_generate_integers():
    assert generate_integers(2, 5) == [2, 3, 4, 5]
