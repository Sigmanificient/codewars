"""Kata url: https://www.codewars.com/kata/53f1015fa9fe02cbda00111a."""

from random import choice


class Ghost:

    def __init__(self):
        self.color: str = choice(("white", "yellow", "purple", "red"))
