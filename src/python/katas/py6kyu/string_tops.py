"""Kata url: https://www.codewars.com/kata/59b7571bbf10a48c75000070."""


def tops(msg: str) -> str:
    out = ''
    i = j = 1
    while i < len(msg):
        out += msg[i]
        i = i + (2 * j) + 3
        j += 2

    return out[::-1]


def test_tops():
    assert tops("") == ""
    assert tops("12") == "2"
    assert tops("abcdefghijklmnopqrstuvwxyz12345") == "3pgb"
    assert tops("abcdefghijklmnopqrstuvwxyz1236789ABCDEFGHIJKLMN") == "M3pgb"
