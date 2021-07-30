"""Kata url: https://www.codewars.com/kata/57f222ce69e09c3630000212."""

from typing import List


def well(x: List[str]) -> str:
    if not x.count('good'):
        return 'Fail!'

    if x.count('good') <= 2:
        return 'Publish!'

    return 'I smell a series!'
