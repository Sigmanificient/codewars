"""Kata url: https://www.codewars.com/kata/53417de006654f4171000587."""

from typing import List

CARDS = "23456789TJQKA"


def winner(deck_steve: List[str], deck_josh: List[str]) -> str:
    j = s = 0

    for a, b in zip(deck_steve, deck_josh):
        p = CARDS.index(a) - CARDS.index(b)

        j += p < 0
        s += p > 0

    if j == s:
        return 'Tie'

    if s > j:
        return f"Steve wins {s} to {j}"

    return f"Josh wins {j} to {s}"


def test_winner():
    assert winner(
        ['2', '3', '4', '5', '6'], ['7', '8', '9', 'T', 'J']
    ) == "Josh wins 5 to 0"

    assert winner(
        ['7', '4', '3', 'T', 'J', 'Q'], ['8', '9', '2', '5', '6', '2']
    ) == "Steve wins 4 to 2"

    assert winner(
        ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'],
        ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'][::-1]
    ) == "Tie"
