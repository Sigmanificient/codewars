"""Kata url: https://www.codewars.com/kata/5938f5b606c3033f4700015a."""

RESULT_LEFT = "Left side wins"
RESULT_RIGHT = "Right side wins"
RESULT_DRAW = "Let's fight again!"


def alphabet_war(fight: str) -> str:
    warriors = 'wpbs*zdqm'
    survivors = []

    size = len(fight) - 1
    for c, char in enumerate(fight):
        if char == '*':
            continue

        if c and fight[c - 1] == '*':
            continue

        if c < size and fight[c + 1] == '*':
            continue

        survivors.append(char)

    point = sum((warriors.index(w) - 4) for w in survivors if w in warriors)
    if not point:
        return RESULT_DRAW

    return RESULT_LEFT if point > 0 else RESULT_RIGHT


def test_alphabet_war():
    assert alphabet_war("z") == RESULT_RIGHT
    assert alphabet_war("****") == RESULT_DRAW
    assert alphabet_war("z*dq*mw*pb*s") == RESULT_DRAW
    assert alphabet_war("zdqmwpbs") == RESULT_DRAW
    assert alphabet_war("zz*zzs") == RESULT_RIGHT
    assert alphabet_war("sz**z**zs") == RESULT_LEFT
    assert alphabet_war("z*z*z*zs") == RESULT_LEFT
    assert alphabet_war("*wwcwwww*z*") == RESULT_LEFT
    assert alphabet_war("vw****z") == RESULT_DRAW
    assert alphabet_war("mb**qwwp**dma") == RESULT_DRAW