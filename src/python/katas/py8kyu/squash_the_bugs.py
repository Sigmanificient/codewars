"""Kata url: https://www.codewars.com/kata/56f173a35b91399a05000cb7."""


def find_longest(string: str) -> int:
    return max(len(x) for x in string.split())


def test_find_longest():
    assert find_longest("The quick white fox jumped around the massive dog") == 7
    assert find_longest("Take me to tinseltown with you") == 10
    assert find_longest("Sausage chops") == 7
    assert find_longest("Wind your body and wiggle your belly") == 6
    assert find_longest("Lets all go on holiday") == 7
