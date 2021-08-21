"""Kata url: https://www.codewars.com/kata/55d277882e139d0b6000005d."""

from typing import List


def find_average(nums: List[int]) -> float:
    return (sum(nums) / len(nums)) if nums else 0