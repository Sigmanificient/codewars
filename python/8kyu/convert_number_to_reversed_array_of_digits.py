"""Kate url: https://www.codewars.com/kata/5583090cbe83f4fd8c000051."""

from typing import List


def digitize(n: int) -> List[int]:
    return list(map(int, str(n)))[::-1]
