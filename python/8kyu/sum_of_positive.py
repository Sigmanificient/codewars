from typing import List


def positive_sum(arr: List[int]) -> int:
    """Kata url: https://www.codewars.com/kata/5715eaedb436cf5606000381."""
    return sum(x for x in arr if x > 0)
