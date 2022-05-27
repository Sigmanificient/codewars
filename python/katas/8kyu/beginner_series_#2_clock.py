"""Kata url: https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a."""


def past(h: int, m: int, s: int) -> int:
    return (h * 3600 + m * 60 + s) * 1000
