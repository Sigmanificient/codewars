from typing import List


def solution(string: str, markers: List[str]) -> str:
    """Kata url: https://www.codewars.com/kata/51c8e37cee245da6b40000bd."""
    stripped: List[str] = []

    for line in string.split('\n'):
        new_lines: List[str] = [
            line[::-1].partition(marker)[2][::-1] for marker in markers if marker in line
        ]

        if not new_lines:
            stripped.append(line)
            continue

        stripped.append(min(new_lines))

    return '\n'.join(line.strip() for line in stripped)
