"""Kata url: https://www.codewars.com/kata/559536379512a64472000053."""

charset: str = "abcdefghijklmnopqrstuvwxyz"


def play_pass(s: str, n: int) -> str:
    string: str = ''
    for c, char in enumerate(s):
        char = char.lower()

        if char.isdigit():
            char = str(9 - int(char))

        if char in charset:
            char = charset[(charset.index(char) + n) % len(charset)]

        string = f'{char if c % 2 else char.upper()}{string}'
    return string
