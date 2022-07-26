"""Kata url: https://www.codewars.com/kata/56b0ff16d4aa33e5bb00008e."""


def shorten_to_date(long_date: str) -> str:
    return long_date.split(",")[0]


def test_shorten_to_date():
    assert shorten_to_date("Monday February 2, 8pm") == "Monday February 2"
    assert shorten_to_date("Tuesday May 29, 8pm") == "Tuesday May 29"
    assert shorten_to_date("Wed September 1, 3am") == "Wed September 1"
    assert shorten_to_date("Friday May 2, 9am") == "Friday May 2"
    assert shorten_to_date("Tuesday January 29, 10pm") == "Tuesday January 29"
