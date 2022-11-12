"""Kata url: https://www.codewars.com/kata/55eeddff3f64c954c2000059."""


def sum_consecutives(s):
    sum_ = p = s[0]

    track = []
    for c in s[1::]:
        if c == p:
            sum_ += c
            continue
        track.append(sum_)
        sum_ = c
        p = c

    track.append(sum_)
    return track


def test_sum_consecutive():
    assert sum_consecutives([1, 4, 4, 4, 0, 4, 3, 3, 1]) == [1, 12, 0, 4, 6, 1]
    assert sum_consecutives([1, 1, 7, 7, 3]) == [2, 14, 3]
    assert sum_consecutives([-5, -5, 7, 7, 12, 0]) == [-10, 14, 12, 0]
    assert sum_consecutives([3, 3, 3, 3, 1]) == [12, 1]
