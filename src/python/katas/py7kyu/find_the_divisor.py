"""Kata url: https://www.codewars.com/kata/544aed4c4a30184e960010f4."""
from typing import List, Union


def divisors(n: int) -> Union[str, List[int]]:
    return [i for i in range(2, n) if not n % i] or f"{n} is prime"


def test_divisors():
    assert divisors(15) == [3, 5]
    assert divisors(253) == [11, 23]
    assert divisors(24) == [2, 3, 4, 6, 8, 12]
    assert divisors(25) == [5]
    assert divisors(13) == "13 is prime"
    assert divisors(3) == "3 is prime"
    assert divisors(29) == "29 is prime"
