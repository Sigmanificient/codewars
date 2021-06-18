from typing import List


def index(array: List[int], n: int) -> int:
    """Kata url: https://www.codewars.com/kata/57d814e4950d8489720008db."""
    return array[n] ** n if (len(array) > n) else -1
