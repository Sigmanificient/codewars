"""Kata url: https://www.codewars.com/kata/599febdc3f64cd21d8000117."""

digits = [
    "zero", "one", "two", "three", "four",
    "five", "six", "seven", "eight", "nine"
]


def digits_str(n):
    return ''.join(digits[k] for k in map(int, str(n)))


def numbers_of_letters(n):
    n_str = digits_str(n)
    out = [n_str]

    while n_str != "four":
        n = len(n_str)
        n_str = digits_str(n)
        out.append(n_str)

    return out


def test_numbers_of_letters():
    assert numbers_of_letters(1) == ["one", "three", "five", "four"]
    assert numbers_of_letters(12) == ["onetwo", "six", "three", "five", "four"]
    assert numbers_of_letters(37) == [
        "threeseven", "onezero", "seven", "five", "four"
    ]
    assert numbers_of_letters(311) == [
        'threeoneone', 'oneone', 'six', 'three', 'five', 'four'
    ]
    assert numbers_of_letters(999) == [
        "nineninenine", "onetwo", "six", "three", "five", "four"
    ]
