from typing import List


def get_average(marks: List[int]) -> int:
    """Kata url: https://www.codewars.com/kata/563e320cee5dddcf77000158."""
    return sum(marks) // len(marks)
