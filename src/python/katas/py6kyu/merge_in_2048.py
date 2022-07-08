"""Kata url: https://www.codewars.com/kata/55e1990978c60e5052000011."""


def merge(line):
    out = [x for x in line if x]
    out += [0] * (len(line) - len(out))

    for i in range(len(line) - 1):
        a = out[i]
        b = out[i + 1]

        if a == b:
            out[i] = a * 2
            out[i + 1] = 0

    out = [x for x in out if x]
    out += [0] * (len(line) - len(out))
    return out


def test_merge():
    assert merge([2, 0, 2, 2]) == [4, 2, 0, 0]
    assert merge([2, 0, 2, 4]) == [4, 4, 0, 0]
    assert merge([0, 0, 2, 2]) == [4, 0, 0, 0]
