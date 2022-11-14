"""Kata url: https://www.codewars.com/kata/5a9e86705ee396d6be000091."""


def check_three_and_two(array):
    return (
        len(set(array)) == 2
        and array.count(array[0]) in {2, 3}
    )


def test_check_three_and_two():
    assert check_three_and_two(["a", "a", "a", "b", "b"])
    assert not check_three_and_two(["a", "c", "a", "c", "b"])
    assert not check_three_and_two(["a", "a", "a", "a", "a"])
    assert not check_three_and_two(["c", "a", "a", "a", "a"])
