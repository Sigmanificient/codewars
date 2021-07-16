from typing import List


def perimeter(n: int) -> int:
    """Kata url: https://www.codewars.com/kata/559a28007caad2ac4e000083."""
    r: List[int] = []
    a = b = 1
    c: int = n + 1
    while c:
        r.append(a)
        a, b = b, a + b
        c -= 1
    return 4 * sum(r)
