"""Kata url: https://www.codewars.com/kata/5300901726d12b80e8000498."""

from typing import Union, List


def fizzbuzz(n: int) -> List[Union[str, int]]:
    return ["Fizz" * (not i % 3) + "Buzz" * (not i % 5) or i for i in range(1, n + 1)]


def test_fizzbuzz():
    expected = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz"]
    assert fizzbuzz(10) == expected
