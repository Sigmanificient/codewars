"""Kata url: https://www.codewars.com/kata/563a631f7cbbc236cf0000c2."""


def move(position: int, roll: int) -> int:
    return roll * 2 + position


def test_move():
    assert move(0, 0) == 0
    assert move(0, 4) == 8
    assert move(3, 6) == 15
    assert move(2, 5) == 12
