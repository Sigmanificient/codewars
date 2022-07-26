"""Kata url: https://www.codewars.com/kata/56dae9dc54c0acd29d00109a."""


def main(verb: str, noun: str) -> str:
    return verb + noun


def test_main():
    assert main("take ", "item") == "take item"
    assert main("use ", "sword") == "use sword"
    assert main("drop ", "item") == "drop item"
    assert main("go ", "north") == "go north"
    assert main("go ", "south") == "go south"
