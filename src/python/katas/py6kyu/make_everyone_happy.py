"""Kata url: https://www.codewars.com/kata/61eeb6e7577f050037b17a2d."""
MOUTHS, NOSES, EYES = '([', '-~', ':;='


def smile(text):
    out = ''

    for c, char in enumerate(text):
        if char not in MOUTHS or not c:
            out += char
            continue

        if text[c - 1] in EYES:
            out += ')' if char == '(' else ']'
        elif c > 1 and text[c - 1] in NOSES and text[c - 2] in EYES:
            out += ')' if char == '(' else ']'
        else:
            out += char
    return out


def test_smile():
    assert smile("Howdy :(") == "Howdy :)"
    assert smile("Never be sad =[") == "Never be sad =]"
    assert smile(
        "Change this `=(` and this `:[`"
    ) == "Change this `=)` and this `:]`"
