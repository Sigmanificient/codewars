charset: str = "abcdefghijklmnopqrstuvwxyz"


def play_pass(s: str, n: int) -> str:
    """Kata url: https://www.codewars.com/kata/559536379512a64472000053."""
    string: str = ''
    for c, char in enumerate(s):
        char: str = char.lower()

        if char.isdigit():
            char = str(9 - int(char))

        if char in charset:
            char: str = charset[(charset.index(char) + n) % len(charset)]

        string: str = f'{char if c % 2 else char.upper()}{string}'
    return string
