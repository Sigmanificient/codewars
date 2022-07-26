"""Kata url: https://www.codewars.com/kata/57f222ce69e09c3630000212."""

from typing import List


def well(x: List[str]) -> str:
    if not x.count("good"):
        return "Fail!"

    if x.count("good") <= 2:
        return "Publish!"

    return "I smell a series!"


def test_well():
    args = {"g": "good", "b": "bad"}

    def prepare(x: List[str]) -> List[str]:
        return list(map(args.__getitem__, x))

    assert well(prepare("bbb")) == "Fail!"
    assert well(prepare("gbbbb")) == "Publish!"
    assert well(prepare("gbbbbgbbg")) == "I smell a series!"
