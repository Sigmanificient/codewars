from typing import List


def first_non_consecutive(arr: List[int]) -> int:
    """Kata url: https://www.codewars.com/kata/58f8a3a27a5c28d92e000144."""
    for element, following in zip(arr, arr[1:]):
        if element + 1 != following:
            return following
