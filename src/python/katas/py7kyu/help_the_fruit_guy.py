"""Kata url: https://www.codewars.com/kata/557af4c6169ac832300000ba."""


def remove_rotten(bag_of_fruits):
    return [
        f[6 * f.startswith('rotten'):].lower()
        for f in (bag_of_fruits or [])
    ]


def test_remove_rotten():
    assert remove_rotten(
        ["apple", "banana", "kiwi", "melone", "orange"]
    ) == ["apple", "banana", "kiwi", "melone", "orange"]

    assert remove_rotten([
        "rottenApple", "rottenBanana", "rottenApple",
        "rottenPineapple", "rottenKiwi"
    ]) == ["apple", "banana", "apple", "pineapple", "kiwi"]

    assert remove_rotten([]) == []
    assert remove_rotten(None) == []

    assert remove_rotten(
        ["apple", "rottenBanana", "rottenApple", "pineapple", "kiwi"]
    ) == ["apple", "banana", "apple", "pineapple", "kiwi"]
