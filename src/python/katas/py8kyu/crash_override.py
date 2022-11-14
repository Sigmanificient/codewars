"""Kata url: https://www.codewars.com/kata/578c1e2edaa01a9a02000b7f."""
from string import ascii_uppercase


SURNAME = {
    'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst', 'D': 'Discharge',
    'E': 'Electron', 'F': 'Faraday', 'G': 'Gig', 'H': 'Hacker', 'I': 'IP',
    'J': 'Jabber', 'K': 'Killer', 'L': 'Lazer', 'M': 'Mike',  'N': 'n00b',
    'O': 'Overclock', 'P': 'Payload', 'Q': 'Quark', 'R': 'Roy', 'S': 'Spy',
    'T': 'T-Rex', 'U': 'Unit', 'V': 'Virus', 'W': 'Worm', 'X': 'X',
    'Y': 'Yob', 'Z': 'Zombie'
}

FIRST_NAME = {
    'A': 'Alpha', 'B': 'Beta', 'C': 'Cache', 'D': 'Data', 'E': 'Energy',
    'F': 'Function', 'G': 'Glitch', 'H': 'Half-life', 'I': 'Ice', 'J': 'Java',
    'K': 'Keystroke', 'L': 'Logic', 'M': 'Malware', 'N': 'Nagware', 'O': 'OS',
    'P': 'Phishing', 'Q': 'Quantum', 'R': 'RAD', 'S': 'Strike', 'T': 'Trojan',
    'U': 'Ultraviolet', 'V': 'Vanilla', 'W': 'WiFi', 'X': 'Xerox', 'Y': 'Y',
    'Z': 'Zero'
}


def alias_gen(f_name, l_name):
    f, l = f_name[0].upper(), l_name[0].upper()

    if f not in ascii_uppercase or l not in ascii_uppercase:
        return 'Your name must start with a letter from A - Z.'
    return FIRST_NAME[f] + ' ' + SURNAME[l]


def test_alias_gen():
    assert alias_gen('Mike', 'Millington') == 'Malware Mike'
    assert alias_gen('Fahima', 'Tash') == 'Function T-Rex'
    assert alias_gen('Daisy', 'Petrovic') == 'Data Payload'
    assert alias_gen('Barny', 'White') == 'Beta Worm'
    assert alias_gen('Hank', 'Kutz') == 'Half-life Killer'
    assert alias_gen('walter', 'white') == 'WiFi Worm'
    assert alias_gen(
        '123abc', 'Pinkman'
    ) == 'Your name must start with a letter from A - Z.'
