"""Kata url: https://www.codewars.com/kata/57e76bc428d6fbc2d500036d."""

from typing import List


def string_to_array(s: str) -> List[str]:
    return s.split() if s else ['']
