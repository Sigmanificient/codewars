"""Kata url: https://www.codewars.com/kata/5710443187a36a9cee0005a1."""


def sc(width, length, gaps):
    p = 2 * width + 2 * (length - 2)

    if not gaps:
        return p

    d, r = divmod(p, gaps + 1)
    return d * (r == 0)


def test_sc():
    assert sc(3, 3, 1) == 4
    assert sc(3, 3, 3) == 2
    assert sc(3, 3, 2) == 0
    assert sc(7, 7, 3) == 6
    assert sc(3, 3, 0) == 8
    assert sc(3, 3, 10) == 0
    assert sc(2, 2, 1) == 2
    assert sc(2, 2, 0) == 4
    assert sc(200, 2, 1) == 200
    assert sc(2, 200, 1) == 200
