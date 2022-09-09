"""Kata url: https://www.codewars.com/kata/58f0ba42e89aa6158400000e."""


def fold_to(distance):
    if distance < 0:
        return None

    thickness = 0.0001
    n = 0

    while distance > thickness:
        thickness *= 2
        n += 1

    return n


def test_fold_to():
    assert fold_to(384000000) == 42
    assert fold_to(0.00005) == 0
    assert fold_to(0.0000001) == 0
    assert fold_to(0) == 0
    assert fold_to(-1) is None
