"""Kata url: https://www.codewars.com/kata/52fb87703c1351ebd200081f."""
import math


def what_century(year):
    century = math.ceil(int(year) / 100)

    ordinal = {'1': 'st', '2': 'nd', '3': 'rd'}.get(
        str(century)[-1] * (11 > century or century > 13), 'th'
    )

    return f"{century}{ordinal}"


def test_what_century():
    assert what_century("1999") == "20th"
    assert what_century("2000") == "20th"
    assert what_century("6700") == "67th"
    assert what_century("2011") == "21st"
    assert what_century("2154") == "22nd"
    assert what_century("2259") == "23rd"
    assert what_century("1234") == "13th"
    assert what_century("1023") == "11th"
