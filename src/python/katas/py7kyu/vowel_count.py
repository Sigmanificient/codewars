"""Kata url: https://www.codewars.com/kata/54ff3102c1bad923760001f3."""


def getCount(sentence: str) -> int:
    return sum(sentence.count(v) for v in "aeiou")
