"""Kata url: https://www.codewars.com/kata/57a60bad72292d3e93000a5a."""


def to_acronym(inp: str) -> str:
    return ''.join(x[0] for x in inp.split(' ')).upper()


def test_to_acronym():
    assert to_acronym("") == ""
    assert to_acronym("Code Wars") == "CW"
    assert to_acronym("Water Closet") == "WC"
    assert to_acronym("Portable Network Graphics") == "PNG"
    assert to_acronym("PHP: Hypertext Preprocessor") == "PHP"
    assert to_acronym("hyper text markup language") == "HTML"
    assert to_acronym("Ruby on Rails") == "ROR"

    assert to_acronym("First In, First Out") == "FIFO"
    assert to_acronym("GNU Image Manipulation Program") == "GIMP"
