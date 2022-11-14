"""Kata url: https://www.codewars.com/kata/568018a64f35f0c613000054."""
import pytest


class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives

    def guess(self, n):
        if not self.lives:
            raise ValueError("Omae wa mo shindeiru")

        self.lives -= (t := n != self.number)
        return not t


def test_guesser():
    guesser = Guesser(10, 2)
    guesser.guess(10)
    guesser.guess(10)
    guesser.guess(10)
    guesser.guess(10)
    assert guesser.guess(10)

    guesser = Guesser(10, 2)
    guesser.guess(1)
    assert not guesser.guess(1)

    guesser = Guesser(10, 2)
    guesser.guess(1)
    guesser.guess(2)

    with pytest.raises(ValueError):
        guesser.guess(10)
