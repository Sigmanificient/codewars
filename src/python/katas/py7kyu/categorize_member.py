"""Kata url: https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa."""


def open_or_senior(data):
    return ["Senior" if p[0] >= 55 and p[1] > 7 else "Open" for p in data]


def test_open_or_senior():
    assert open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)]) == [
        "Open",
        "Senior",
        "Open",
        "Senior",
    ]

    assert open_or_senior([(16, 23), (73, 1), (56, 20), (1, -1)]) == [
        "Open",
        "Open",
        "Senior",
        "Open",
    ]
