"""Kata url: https://www.codewars.com/kata/5268af3872b786f006000228."""

from random import randint, seed

seed(0)
guess = randint(1, 100)
seed(0)


def test_solution():
    lucky_number = randint(1, 100)
    assert guess == lucky_number
