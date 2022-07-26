"""Kata url: https://www.codewars.com/kata/5412509bd436bd33920011bc."""


def maskify(cc: str) -> str:
    return cc[-4:].rjust(len(cc), "#")


def test_maskify():
    assert maskify("") == ""
    assert maskify("1") == "1"
    assert maskify("64607935616") == "#######5616"
    assert maskify("4556364607935616") == "############5616"
    assert maskify("SF$SDfgsd2eA") == "########d2eA"
