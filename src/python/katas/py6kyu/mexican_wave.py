"""Kata url: https://www.codewars.com/kata/58f5c63f1e26ecda7e000029."""
from typing import List


def wave(people: str) -> List[str]:
    return [
        "".join(chr.upper() if c == i else chr for c, chr in enumerate(people))
        for i, current_chr in enumerate(people)
        if current_chr != " "
    ]


def test_wave():
    assert wave("") == []
    assert wave("hello") == ["Hello", "hEllo", "heLlo", "helLo", "hellO"]

    assert wave("codewars") == [
        "Codewars",
        "cOdewars",
        "coDewars",
        "codEwars",
        "codeWars",
        "codewArs",
        "codewaRs",
        "codewarS",
    ]

    assert wave("two words") == [
        "Two words",
        "tWo words",
        "twO words",
        "two Words",
        "two wOrds",
        "two woRds",
        "two worDs",
        "two wordS",
    ]

    assert wave(" gap ") == [" Gap ", " gAp ", " gaP "]
