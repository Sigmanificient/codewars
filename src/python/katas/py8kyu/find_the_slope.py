"""Kata url: https://www.codewars.com/kata/55a75e2d0803fea18f00009d."""


def find_slope(points):
    a, b, c, d = points
    if y := (a - c):
        return str((b - d) // y)
    return "undefined"


def test_find_slope():
    assert find_slope([12, -18, -15, -18]) == "0"
    assert find_slope([3, -20, 5, 8]) == "14"
    assert find_slope([17, -3, 17, 8]) == "undefined"
    assert find_slope([1, -19, -2, -7]) == "-4"
    assert find_slope([19, 3, 20, 3]) == "0"
    assert find_slope([6, -12, 15, -3]) == "1"
    assert find_slope([15, -3, 15, -3]) == "undefined"
    assert find_slope([9, 3, 19, -17]) == "-2"
    assert find_slope([3, 6, 4, 10]) == "4"
    assert find_slope([2, 7, 4, -7]) == "-7"
