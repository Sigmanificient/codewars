"""Kata url: https://www.codewars.com/kata/5667e8f4e3f572a8f2000039."""


def accum(s: str) -> str:
    return "-".join((x * (i + 1)).capitalize() for i, x in enumerate(s))


def test_accum():
    assert accum("abcd") == "A-Bb-Ccc-Dddd"
    assert accum("RqaEzty") == "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
    assert accum("cwAt") == "C-Ww-Aaa-Tttt"
