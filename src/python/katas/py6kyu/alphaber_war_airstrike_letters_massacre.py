"""Kata url: https://www.codewars.com/kata/5938f5b606c3033f4700015a."""


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
        return "Let's fight again!"

    return f"{'Right' if point > 0 else 'Left'} side wins!"


def test_alphabet_war():
    assert alphabet_war("z") == "Right side wins!"
    assert alphabet_war("****") == "Let's fight again!"
    assert alphabet_war("z*dq*mw*pb*s") == "Let's fight again!"
    assert alphabet_war("zdqmwpbs") == "Let's fight again!"
    assert alphabet_war("zz*zzs") == "Right side wins!"
    assert alphabet_war("sz**z**zs") == "Left side wins!"
    assert alphabet_war("z*z*z*zs") == "Left side wins!"
    assert alphabet_war("*wwcwwww*z*") == "Left side wins!"
    assert alphabet_war("vw****z") == "Let's fight again!"
    assert alphabet_war("mb**qwwp**dma") == "Let's fight again!"