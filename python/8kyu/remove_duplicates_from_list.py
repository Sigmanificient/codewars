from typing import List


def distinct(seq: List[int]) -> List[int]:
    """Kata url: https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118."""
    res = []
    for item in seq:
        if item not in res:
            res.append(item)

    return res
