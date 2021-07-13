from typing import Union, List


def fizzbuzz(n: int) -> List[Union[str, int]]:
    """Kata url: https://www.codewars.com/kata/5300901726d12b80e8000498"""
    return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or i for i in range(1, n + 1)]