"""Kata url: https://www.codewars.com/kata/5a360620f28b82a711000047."""


def define_suit(card):
    return {"C": "clubs", "S": "spades", "D": "diamonds", "H": "hearts"}[card[-1]]


def test_define_suit():
    assert define_suit("3C") == "clubs"
    assert define_suit("QS") == "spades"
    assert define_suit("9D") == "diamonds"
    assert define_suit("JH") == "hearts"
