from typing import List


def digitize(n: int) -> List[int]:
    """Kate url: https://www.codewars.com/kata/5583090cbe83f4fd8c000051."""
    return list(map(int, str(n)))[::-1]
