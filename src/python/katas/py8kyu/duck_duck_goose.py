"""Kata url: https://www.codewars.com/kata/582e0e592029ea10530009ce."""


def duck_duck_goose(players, goose):
    return players[(goose - 1) % len(players)].name


def test_duck_duck_goose():
    class Player:

        def __init__(self, name: str):
            self.name = name

    players = [Player(x) for x in "abcdcefghz"]

    assert duck_duck_goose(players, 1) == "a"
    assert duck_duck_goose(players, 3) == "c"
    assert duck_duck_goose(players, 10) == "z"
    assert duck_duck_goose(players, 20) == "z"
    assert duck_duck_goose(players, 30) == "z"
    assert duck_duck_goose(players, 18) == "g"
    assert duck_duck_goose(players, 28) == "g"
    assert duck_duck_goose(players, 12) == "b"
    assert duck_duck_goose(players, 2) == "b"
    assert duck_duck_goose(players, 7) == "f"
