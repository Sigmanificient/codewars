"""Kata url: https://www.codewars.com/kata/59dd3ccdded72fc78b000b25."""

from typing import List

week: List[str] = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
]


def whatday(num: int) -> str:
    if num < 1 or num > 7:
        return "Wrong, please enter a number between 1 and 7"

    return week[num - 1]


def test_whatday():
    assert whatday(1) == "Sunday"
    assert whatday(2) == "Monday"
    assert whatday(3) == "Tuesday"
    assert whatday(8) == "Wrong, please enter a number between 1 and 7"
    assert whatday(20) == "Wrong, please enter a number between 1 and 7"
