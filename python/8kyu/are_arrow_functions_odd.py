"""Kata url: https://www.codewars.com/kata/559f80b87fa8512e3e0000f5."""

from typing import Callable, List

odds: Callable[[List[int]], List[int]] = lambda arr: [x for x in arr if x % 2]
