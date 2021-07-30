"""Kata url: https://www.codewars.com/kata/556deca17c58da83c00002db."""

from typing import List


def tribonacci(signature: List[int], n: int) -> List[int]:
    if n == 0:
        return []

    if n < 3:
        return signature[:n]

    for i in range(n - 3):
        signature.append(sum(signature[i:i + 3]))

    return signature
