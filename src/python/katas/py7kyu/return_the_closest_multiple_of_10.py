"""Kata url: https://www.codewars.com/kata/58249d08b81f70a2fc0001a4."""


def closest_multiple_10(i: int) -> int:
    return round(i / 10) * 10


def test_closest_multiple_10():
    for i in range(10, 15):
        assert closest_multiple_10(i) == 10

    for i in range(15, 25):
        assert closest_multiple_10(i) == 20
