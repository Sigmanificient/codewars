"""Kata url: https://www.codewars.com/kata/587731fda577b3d1b0001196."""


def camel_case(string: str) -> str:
    return "".join(w.capitalize() for w in string.split(" "))


def test_camel_case():
    assert camel_case("") == ""
    assert camel_case("test case") == "TestCase"
    assert camel_case("camel case method") == "CamelCaseMethod"
    assert camel_case("say hello ") == "SayHello"
    assert camel_case(" camel case word") == "CamelCaseWord"
