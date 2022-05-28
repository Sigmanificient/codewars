# Kata url: https://www.codewars.com/kata/57ab3c09bb994429df000a4a.

from typing import List


def two_highest(arg1: List[int]) -> List[int]:
    return sorted(set(arg1), reverse=True)[:2]
