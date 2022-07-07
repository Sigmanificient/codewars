"""Kata url: https://www.codewars.com/kata/529eef7a9194e0cbc1000255."""


def is_anagram(test: str, original: str) -> bool:
    return sorted(test.lower()) == sorted(original.lower())


def test_is_anagram():
    assert is_anagram("foefet", "toffee")
    assert is_anagram("Buckethead", "DeathCubeK")
    assert is_anagram("Twoo", "WooT")
    assert not is_anagram("dumble", "bumble")
    assert not is_anagram("ound", "round")
    assert not is_anagram("apple", "pale")
