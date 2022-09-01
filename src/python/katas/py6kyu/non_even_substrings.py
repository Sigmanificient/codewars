"""Kata url: https://www.codewars.com/kata/59da47fa27ee00a8b90000b4."""


def solve(s):
    return sum(
        int(s[i: off + i]) % 2
        for off in range(1, len(s) + 1)
        for i in range(len(s) - off + 1)
    )


def test_solve():
    assert solve("1347") == 7
    assert solve("1357") == 10
    assert solve("13471") == 12
    assert solve("134721") == 13
    assert solve("1347231") == 20
    assert solve("13472315") == 28
