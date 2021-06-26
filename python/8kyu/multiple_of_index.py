from typing import List


def multiple_of_index(arr: List[int]) -> List[int]:
    """Kata url: https://www.codewars.com/kata/5a34b80155519e1a00000009."""
    return [x for c, x in enumerate(arr[1::]) if not (x / (c + 1)) % 1]
