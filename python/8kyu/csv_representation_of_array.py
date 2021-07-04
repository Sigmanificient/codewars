from typing import List


def to_csv_text(array: List[List[int]]) -> str:
    """Kata url: https://www.codewars.com/kata/5a34af40e1ce0eb1f5000036."""
    return '\n'.join(
        ','.join(str(item) for item in line) for line in array
    )
