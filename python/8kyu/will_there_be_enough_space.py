"""Kata url: https://www.codewars.com/kata/5875b200d520904a04000003."""


def enough(cap: int, on: int, wait: int) -> int:
    is_enough: bool = (cap - on) > wait
    return 0 if is_enough else abs((cap - on) - wait)
