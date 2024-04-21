"""Kata url: https://www.codewars.com/kata/52c31f8e6605bcc646000082."""


def two_sum(numbers, target):
    return next(
        (
            [off - 1, off + c]
            for off, t in enumerate(numbers, start=1)
            for c, i in enumerate(numbers[off:])
            if t + i == target
        ),
        [],
    )


def test_two_sum():
    assert sorted(two_sum([1, 2, 3], 4)) == [0, 2]
    assert sorted(two_sum([1234, 5678, 9012], 14690)) == [1, 2]
    assert sorted(two_sum([2, 2, 3], 4)) == [0, 1]