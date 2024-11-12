"""Kata url: https://www.codewars.com/kata/51edd51599a189fe7f000015."""

def solution(array_a: list[int], array_b: list[int]) -> float:
    return sum((b - a)**2 for a, b in zip(array_a, array_b)) / len(array_a)