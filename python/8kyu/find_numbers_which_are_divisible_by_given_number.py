from typing import List


def divisible_by(numbers: List[int], divisor: int) -> List[int]:
    """Kata url: https://www.codewars.com/kata/55edaba99da3a9c84000003b."""
    return [n for n in numbers if (n / divisor).is_integer()]
