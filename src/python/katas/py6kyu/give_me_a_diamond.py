"""Kata url: https://www.codewars.com/kata/5503013e34137eeeaa001648."""
from typing import Optional


def diamond(n: int) -> Optional[str]:
    if not n % 2 or n < 0:
        return None

    half = [' ' * ((n - i) // 2) + '*' * i for i in range(1, n + 1, 2)]
    return '\n'.join(half[:-1] + half[::-1]) + '\n'


def test_diamond():
    assert diamond(1) == "*\n"
    assert diamond(2) is None
    assert diamond(3) == " *\n***\n *\n"
    assert diamond(5) == "  *\n ***\n*****\n ***\n  *\n"
    assert diamond(0) is None
    assert diamond(-3) is None
