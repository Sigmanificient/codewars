from typing import Tuple


def seven(m: int) -> Tuple[int, int]:
    """Kata url: https://www.codewars.com/kata/55e6f5e58f7817808e00002e."""
    step = 0
    while m > 99:
        m = (m // 10 - (2 * (m % 10)))
        step += 1
    return m, step
