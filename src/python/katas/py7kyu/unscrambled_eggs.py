"""Kata url: https://www.codewars.com/kata/55ea5650fe9247a2ea0000a7."""


def unscramble_eggs(word: str) -> str:
    out = []
    i = 0

    while i < len(word):
        if word[i:i+3] == 'egg':
            i += 3
        else:
            out += word[i]
            i += 1
    return ''.join(out)


def test_unscramble_eggs():
    assert unscramble_eggs("ceggodegge heggeregge") == "code here"
    assert unscramble_eggs("FeggUNegg KeggATeggA") == "FUN KATA"
