"""Kara url: https://www.codewars.com/kata/56968ce7753513604b000055."""


def pyramid_height(n):
    c = 1
    while n > 0:
        c += 1
        n -= c ** 2

    return c - 1


def test_pyramid_height():
    assert pyramid_height(1) == 1
    assert pyramid_height(4) == 1
    assert pyramid_height(5) == 2
    assert pyramid_height(29) == 3
    assert pyramid_height(30) == 4
    assert pyramid_height(31) == 4
    assert pyramid_height(1240) == 15
    assert pyramid_height(1241) == 15
    assert pyramid_height(1239) == 14
    assert pyramid_height(1496) == 16
    assert pyramid_height(1495) == 15
    assert pyramid_height(4324) == 23
    assert pyramid_height(4323) == 22
    assert pyramid_height(4899) == 23
    assert pyramid_height(4900) == 24
    assert pyramid_height(5524) == 24
    assert pyramid_height(5525) == 25
    assert pyramid_height(6200) == 25
    assert pyramid_height(6201) == 26
    assert pyramid_height(6254) == 26
