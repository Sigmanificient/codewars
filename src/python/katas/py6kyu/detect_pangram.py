"""Kata url: https://www.codewars.com/kata/545cedaa9943f7fe7b000048."""


def is_pangram(s: str) -> bool:
    return (
        "".join(filter(str.isalpha, sorted(set(s.lower()))))
        == "abcdefghijklmnopqrstuvwxyz"
    )


def test_is_pangram():
    assert is_pangram("The quick, brown fox jumps over the lazy dog!")
    assert not is_pangram("This is not a pangram.")
