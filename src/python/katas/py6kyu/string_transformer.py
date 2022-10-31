"""Kata url: https://www.codewars.com/kata/5878520d52628a092f0002d0."""

def string_transformer(s):
    return ' '.join(s.split(' ')[::-1]).swapcase()


def test_string_transformer():
    assert string_transformer("Example string") == "STRING eXAMPLE"
    assert string_transformer("Example Input") == "iNPUT eXAMPLE"
    assert string_transformer(
        "To be OR not to be That is the Question"
    ) == "qUESTION THE IS tHAT BE TO NOT or BE tO"
    assert string_transformer("") == ""
    assert string_transformer(
        "You Know When  THAT  Hotline Bling"
    ) == "bLING hOTLINE  that  wHEN kNOW yOU"
    assert string_transformer(" A b C d E f G ") == " g F e D c B a "
