"""Kata url: https://www.codewars.com/kata/54fe05c4762e2e3047000add."""


class Ship:
    def __init__(self, draft: int, crew: int):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self) -> bool:
        return (self.draft - self.crew * 1.5) > 20


def test_ship():
    assert not Ship(0, 0).is_worth_it()
    assert not Ship(15, 20).is_worth_it()
    assert not Ship(35, 20).is_worth_it()
    assert Ship(100, 20).is_worth_it()
    assert Ship(100, 40).is_worth_it()
