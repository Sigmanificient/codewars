"""Kata url: https://www.codewars.com/kata/5727bb0fe81185ae62000ae3."""


def clean_string(s: str) -> str:
    out = []

    for c in s:
        if c != '#':
            out.append(c)

        elif out:
            out.pop()

    return ''.join(out)


def test_clean_string():
    assert clean_string("") == ""
    assert clean_string("#######") == ""
    assert clean_string('abc#d##c') == "ac"
    assert clean_string('abc####d##c#') == ""
