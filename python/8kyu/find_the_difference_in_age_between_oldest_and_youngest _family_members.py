from typing import Tuple


def difference_in_ages(ages) -> Tuple[int, int, int]:
    """Kata url: https://www.codewars.com/kata/5720a1cb65a504fdff0003e2."""
    mx = max(ages)
    mn = min(ages)
    return mn, mx, mx - mn