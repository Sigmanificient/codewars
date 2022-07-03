"""Kata url: https://www.codewars.com/kata/53f1015fa9fe02cbda00111a."""

from random import choice


class Ghost:

    def __init__(self):
        self.color: str = choice(("white", "yellow", "purple", "red"))


def test_ghost():
    ghosts = [Ghost().color for _ in range(100)]
    assert ghosts.count("white") >= 1
    assert ghosts.count("yellow") >= 1
    assert ghosts.count("purple") >= 1
    assert ghosts.count("red") >= 1
