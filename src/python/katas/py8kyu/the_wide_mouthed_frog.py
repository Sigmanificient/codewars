"""Kata url: https://www.codewars.com/kata/57ec8bd8f670e9a47a000f89."""


def mouth_size(animal: str) -> str:
    return "small" if animal.lower() == "alligator" else "wide"


def test_mouth_size():
    assert mouth_size("toucan") == "wide"
    assert mouth_size("ant bear") == "wide"
    assert mouth_size("alligator") == "small"
