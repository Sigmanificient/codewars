"""Kata url: https://www.codewars.com/kata/55a14f75ceda999ced000048."""


def temple_strings(obj: str, feature: str) -> str:
    return f"{obj} are {feature}"


def test_temple_strings():
    assert temple_strings("Animals","Good") == 'Animals are Good'
    assert temple_strings("Animals","Good") == 'Animals are Good'
    assert temple_strings("You","Special") == 'You are Special'
    assert temple_strings("lives","frozen") == 'lives are frozen'
