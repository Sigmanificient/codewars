"""Kata url: https://www.codewars.com/kata/565f5825379664a26b00007c."""


def get_size(w, h, d):
    return [
        2 * ((w * h) + (w * d) + (d * h)),
        w * h * d
    ]


def test_get_size():
    assert get_size(4, 2, 6) == [88, 48]
    assert get_size(1, 1, 1) == [6, 1]
    assert get_size(1, 2, 1) == [10, 2]
    assert get_size(1, 2, 2) == [16, 4]
    assert get_size(10, 10, 10) == [600, 1000]
