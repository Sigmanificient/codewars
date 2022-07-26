"""Kata url: https://www.codewars.com/kata/56f699cd9400f5b7d8000b55."""

from typing import List


def fix_the_meerkat(arr: List[str]) -> List[str]:
    return arr[::-1]


def test_fix_the_meerkat():
    assert fix_the_meerkat(["tail", "body", "head"]) == ["head", "body", "tail"]
    assert fix_the_meerkat(["tails", "body", "heads"]) == ["heads", "body", "tails"]
    assert fix_the_meerkat(["bottom", "middle", "top"]) == ["top", "middle", "bottom"]
    assert fix_the_meerkat(["lower legs", "torso", "upper legs"]) == [
        "upper legs",
        "torso",
        "lower legs",
    ]
    assert fix_the_meerkat(["ground", "rainbow", "sky"]) == ["sky", "rainbow", "ground"]
