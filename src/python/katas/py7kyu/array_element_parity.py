"""Kata url: https://www.codewars.com/kata/5a092d9e46d843b9db000064."""


def solve(arr):
    for x in arr:
        if -x not in arr:
            return x


def test_solve():
    assert solve([1, -1, 2, -2, 3]) == 3
    assert solve([-3, 1, 2, 3, -1, -4, -2]) == -4
    assert solve([1, -1, 2, -2, 3, 3]) == 3
    assert solve([-110, 110, -38, -38, -62, 62, -38, -38, -38]) == -38
    assert solve([-9, -105, -9, -9, -9, -9, 105]) == -9
