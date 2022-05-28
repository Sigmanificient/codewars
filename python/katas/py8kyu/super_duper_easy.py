"""Kata url: https://www.codewars.com/kata/55a5bfaa756cfede78000026."""

from typing import Union


def problem(a: Union[int, str]) -> Union[int, str]:
    return 'Error' if isinstance(a, str) else a * 50 + 6
