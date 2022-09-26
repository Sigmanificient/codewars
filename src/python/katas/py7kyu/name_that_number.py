"""Kata url: https://www.codewars.com/kata/579ba41ce298a73aaa000255."""

digits = [
    "zero", "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine"
]

teen = [
    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen", "nineteen"
]

tens = [
    "twenty", "thirty", "forty", "fifty",
    "sixty", "seventy", "eighty", "ninety"
]


def name_that_number(x):
    if x < 10:
        return digits[x]

    if x < 20:
        return teen[x - 10]

    d, u = map(int, str(x))
    return f'{tens[d - 2]} {digits[u]}' if u else tens[d - 2]


def test_name_that_number():
    assert name_that_number(1) == 'one'
    assert name_that_number(52) == 'fifty two'
    assert name_that_number(21) == 'twenty one'
    assert name_that_number(99) == 'ninety nine'
    assert name_that_number(0) == 'zero'
    assert name_that_number(53) == 'fifty three'
    assert name_that_number(23) == 'twenty three'
    assert name_that_number(76) == 'seventy six'
