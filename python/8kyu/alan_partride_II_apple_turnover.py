"""Kata url: https://www.codewars.com/kata/580a094553bd9ec5d800007d."""

from typing import Union

hot: str = "It's hotter than the sun!!"
not_hot: str = "Help yourself to a honeycomb Yorkie for the glovebox."


def apple(x: Union[int, str]) -> str:
    return hot if int(x) ** 2 > 1000 else not_hot
