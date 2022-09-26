"""Kata url: https://www.codewars.com/kata/57a62154cf1fa5b25200031e."""
alternate_case = str.swapcase


def test_alternate_case():
    assert alternate_case("ABC"), "abc"
    assert alternate_case(""), ""
    assert alternate_case(" "), " "
    assert alternate_case("Hello World"), "hELLO wORLD"
    assert alternate_case("cODEwARS"), "CodeWars"
    assert alternate_case(
        "i LIKE MAKING KATAS VERY MUCH"
    ) == "I like making katas very much"
