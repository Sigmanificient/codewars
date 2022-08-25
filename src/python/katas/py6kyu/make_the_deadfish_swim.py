"""Kata url: https://www.codewars.com/kata/51e0007c1f9378fa810002a9."""
from typing import List


def parse(data: str) -> List[int]:
    out = []
    cell = 0

    ops = {
        'o': lambda v: out.append(v) or v,
        'i': lambda v: v + 1,
        'd': lambda v: v - 1,
        's': lambda v: v ** 2
    }

    for ins in data:
        func = ops.get(ins)

        if func is None:
            continue

        cell = func(cell)
    return out


def test_parse():
    assert parse("ooo") == [0, 0, 0]
    assert parse("ioioio") == [1, 2, 3]
    assert parse("idoiido") == [0, 1]
    assert parse("isoisoiso") == [1, 4, 25]
    assert parse("codewars") == [0]
