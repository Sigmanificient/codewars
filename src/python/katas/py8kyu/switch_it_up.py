"""Kata url: https://www.codewars.com/kata/5808dcb8f0ed42ae34000031."""


def switch_it_up(number: int) -> str:
    return (
        "Zero",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
    )[number]


def test_switch_it_up():
    assert switch_it_up(0) == "Zero"
    assert switch_it_up(9) == "Nine"
