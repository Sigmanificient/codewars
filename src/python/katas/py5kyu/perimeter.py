"""Kata url: https://www.codewars.com/kata/559a28007caad2ac4e000083."""

from typing import List


def perimeter(n: int) -> int:
    r: List[int] = []
    a = b = 1
    c: int = n + 1
    while c:
        r.append(a)
        a, b = b, a + b
        c -= 1
    return 4 * sum(r)


def test_perimeter():
    assert perimeter(5) == 80
    assert perimeter(7) == 216
    assert perimeter(20) == 114624
    assert perimeter(30) == 14098308
    assert perimeter(100) == 6002082144827584333104
