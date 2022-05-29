"""Kata url: https://www.codewars.com/kata/5412509bd436bd33920011bc."""


def maskify(cc: str) -> str:
    return cc[-4:].rjust(len(cc), '#')
