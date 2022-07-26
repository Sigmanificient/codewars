"""Kata url: https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3."""


def abbrev_name(name: str) -> str:
    return ".".join(word[0].upper() for word in name.split())


def test_abbrev_name():
    assert abbrev_name("Sam Harris") == "S.H"
    assert abbrev_name("patrick feenan") == "P.F"
    assert abbrev_name("Evan C") == "E.C"
    assert abbrev_name("P Favuzzi") == "P.F"
    assert abbrev_name("David Mendieta") == "D.M"
