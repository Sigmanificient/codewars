"""Kata url: https://www.codewars.com/kata/58373ba351e3b615de0001c3."""


def mormons(starting_number, reach, target):
    current = starting_number
    mission = 0

    while current < target:
        current += current * reach
        mission += 1

    return mission


def test_mormons():
    assert mormons(10, 3, 9) == 0
    assert mormons(99, 2, 99) == 0
    assert mormons(40, 2, 120) == 1
    assert mormons(40, 2, 121) == 2
    assert mormons(20000, 2, 7000000000) == 12
