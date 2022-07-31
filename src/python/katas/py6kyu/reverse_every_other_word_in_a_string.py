"""Kata url: https://www.codewars.com/kata/58d76854024c72c3e20000de."""


def reverse_alternate(words: str) -> str:
    return " ".join(w[::-1] if c % 2 else w for c, w in enumerate(words.split()))


def test_reverse_alternate():
    assert reverse_alternate("Did it work?") == "Did ti work?"
    assert (
        reverse_alternate("I really hope it works this time...")
        == "I yllaer hope ti works siht time..."
    )
    assert (
        reverse_alternate("Reverse this string, please!")
        == "Reverse siht string, !esaelp"
    )
    assert reverse_alternate("Have a beer") == "Have a beer"
    assert reverse_alternate("") == ""
