"""Kata url: https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9."""


def find_short(s: str) -> int:
    return len(sorted(s.split(), key=len)[0])
