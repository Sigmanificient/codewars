"""Kata url: https://www.codewars.com/kata/59377c53e66267c8f6000027."""


def alphabet_war(fight: str) -> str:
    points = 'wpbs-zdqm'
    total = sum((points.index(c) - 4) for c in fight if c in points and c != '-')
    if not total:
        return "Let's fight again!"

    return f"{('Left' if total < 0 else 'Right')} side wins!"


def test_alphabet_war():
    assert alphabet_war("z") == "Right side wins!"
    assert alphabet_war("zdqmwpbs") == "Let's fight again!"
    assert alphabet_war("wq") == "Left side wins!"
    assert alphabet_war("zzzzs") == "Right side wins!"
    assert alphabet_war("wwwwww") == "Left side wins!"
