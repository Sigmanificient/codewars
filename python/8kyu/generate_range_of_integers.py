from typing import List


def generate_range(_min: int, _max: int, step: int) -> List[int]:
    """Kata url: https://www.codewars.com/kata/55eca815d0d20962e1000106."""
    return list(range(_min, _max + 1, step))
