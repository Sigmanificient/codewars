# Kata url: https://www.codewars.com/kata/54598d1fcbae2ae05200112c.

from typing import Callable, Any, List


def all(seq: List[Any], fun: Callable[[Any], bool]) -> bool:
    return sum(fun(x) for x in seq) == len(seq)