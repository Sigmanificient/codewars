"""Kata url: https://www.codewars.com/kata/56efc695740d30f963000557."""


def to_alternating_case(string: str) -> str:
    return "".join(char.lower() if char.isupper() else char.upper() for char in string)


def test_to_alternating_case():
    assert to_alternating_case("hello world") == "HELLO WORLD"
    assert to_alternating_case("HELLO WORLD") == "hello world"
    assert to_alternating_case("hello WORLD") == "HELLO world"
    assert to_alternating_case("HeLLo WoRLD") == "hEllO wOrld"
    assert to_alternating_case("12345") == "12345"
    assert to_alternating_case("1a2b3c4d5e") == "1A2B3C4D5E"
    assert (
        to_alternating_case("String.prototype.toAlternatingCase")
        == "sTRING.PROTOTYPE.TOaLTERNATINGcASE"
    )
    assert to_alternating_case(to_alternating_case("Hello World")) == "Hello World"
    assert to_alternating_case("altERnaTIng cAsE") == "ALTerNAtiNG CaSe"
