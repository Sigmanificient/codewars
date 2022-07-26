"""Kata url: https://www.codewars.com/kata/51c8e37cee245da6b40000bd."""
from typing import List


def solution(string: str, markers: List[str]) -> str:
    stripped: List[str] = []

    for line in string.split("\n"):
        new_lines: List[str] = [
            line[::-1].partition(marker)[2][::-1]
            for marker in markers
            if marker in line
        ]

        if not new_lines:
            stripped.append(line)
            continue

        stripped.append(min(new_lines))

    return "\n".join(line.strip() for line in stripped)


def test_solution():
    sol = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
    assert sol == "apples, pears\ngrapes\nbananas"

    assert solution("a #b\nc\nd $e f g", ["#", "$"]) == "a\nc\nd"
