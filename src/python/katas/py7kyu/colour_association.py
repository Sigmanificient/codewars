"""Kata url: https://www.codewars.com/kata/56d6b7e43e8186c228000637."""
from typing import List


def colour_association(arr: List[List[str]]):
    return [{k: v} for k, v in arr]


def test_colour_association():
    assert colour_association(
        [["white", "goodness"], ["blue", "tranquility"]]
    ) == [{'white': "goodness"}, {'blue': "tranquility"}]

    assert colour_association(
        [
            ["red", "energy"],
            ["yellow", "creativity"],
            ["brown", "friendly"],
            ["green", "growth"]
        ]
    ) == [
        {'red': "energy"},
        {'yellow': "creativity"},
        {'brown': "friendly"},
        {'green': "growth"}
    ]

    assert colour_association(
        [["pink", "compassion"], ["purple", "ambition"]]
    ) == [{'pink': "compassion"}, {'purple': "ambition"}]

    assert colour_association(
        [["gray", "intelligence"], ["black", "classy"]]
    ) == [{'gray': "intelligence"}, {'black': "classy"}]

    assert colour_association(
        [["white", "goodness"], ["blue", "goodness"]]
    ) == [{'white': 'goodness'}, {'blue': 'goodness'}]
