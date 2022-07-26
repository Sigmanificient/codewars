"""Kata url: https://www.codewars.com/kata/5803c0c6ab6c20a06f000026."""


def swap_vowel_case(st: str) -> str:
    return "".join(x.swapcase() if x.lower() in "aeoui" else x for x in st)


def test_swap_vowel_case():
    assert swap_vowel_case(" ") == " "
    assert swap_vowel_case("C Is AlIvE!") == "C is alive!"
    assert swap_vowel_case("to") == "tO"
    assert swap_vowel_case("The") == "ThE"
    assert swap_vowel_case("a") == "A"
