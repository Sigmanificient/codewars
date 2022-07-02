"""Kata url: https://www.codewars.com/kata/53af2b8861023f1d88000832."""


def are_you_playing_banjo(name: str) -> str:
    return (
        f"{name} plays banjo"
        if name.lower().startswith('r')
        else f"{name} does not play banjo"
    )


def test_are_you_playing_banjo():
    assert are_you_playing_banjo("John") == "John does not play banjo"
    assert are_you_playing_banjo("martin") == "martin does not play banjo"
    assert are_you_playing_banjo("Rikke") == "Rikke plays banjo"
    assert are_you_playing_banjo("bravo") == "bravo does not play banjo"
    assert are_you_playing_banjo("rolf") == "rolf plays banjo"
