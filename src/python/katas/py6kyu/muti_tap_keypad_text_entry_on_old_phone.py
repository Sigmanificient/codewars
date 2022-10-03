"""Kata url: https://www.codewars.com/kata/54a2e93b22d236498400134b."""


def presses(phrase: str) -> int:
    nb_pressed = {
        'A': 1, 'B': 2, 'C': 3,
        'D': 1, 'E': 2, 'F': 3,
        'G': 1, 'H': 2, 'I': 3,
        'J': 1, 'K': 2, 'L': 3,
        'M': 1, 'N': 2, 'O': 3,
        'P': 1, 'Q': 2, 'R': 3, 'S': 4,
        'T': 1, 'U': 2, 'V': 3,
        'W': 1, 'X': 2, 'Y': 3, 'Z': 4,
        '*': 1, '#': 1, ' ': 1, '0': 2,
        '1': 1, '2': 4, '3': 4,
        '4': 4, '5': 4, '6': 4,
        '7': 5, '8': 4, '9': 5
    }

    return sum(
        nb_pressed.get(char.upper())
        for char in phrase
    )


def test_presses():
    assert presses("LOL") == 9
    assert presses("HOW R U") == 13
    assert presses("WHERE DO U WANT 2 MEET L8R") == 47
    assert presses("lol") == 9
    assert presses("0") == 2
    assert presses("ZER0") == 11
    assert presses("1") == 1
    assert presses("IS NE1 OUT THERE") == 31
    assert presses("#") == 1
    assert presses("#codewars #rocks") == 36
