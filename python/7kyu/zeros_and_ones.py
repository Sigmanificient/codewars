from typing import List


def binary_array_to_number(arr: List[int]) -> int:
    """Kata url: https://www.codewars.com/kata/578553c3a1b8d5c4030003."""
    return int(''.join(map(str, arr)), 2)
