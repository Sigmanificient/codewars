"""Kata url: https://www.codewars.com/kata/52945ce49bb38560fe0001d9."""


def pascal(p):
    line = [1]
    out = [line]

    for _ in range(p - 1):
        tmp = [0] + line + [0]
        line = [x + y for x, y in zip(tmp, tmp[1::])]
        out.append(line)

    return out


def test_pascal():
    assert pascal(5) == [
        [1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]
    ]
    assert pascal(10) == [
        [1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1],
        [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1],
        [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    ]