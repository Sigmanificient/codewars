"""Kata url: https://www.codewars.com/kata/630006e1b4e54c7a7e943679."""


def sierpinski_carpet_string(n):
    base = ['██']

    for i in range(n):
        top_bot = [line * 3 for line in base]
        mid = [
            line + (' ' * len(line)) + line
            for line in base
        ]

        base = top_bot + mid + top_bot

    return '\n'.join(base)


def test_sierpinski_carpet_string():
    assert sierpinski_carpet_string(0) == '██'
    assert sierpinski_carpet_string(1) == (
        '██████\n'
        '██  ██\n'
        '██████'
    )

    assert sierpinski_carpet_string(2) == (
        '██████████████████\n'
        '██  ████  ████  ██\n'
        '██████████████████\n'
        '██████      ██████\n'
        '██  ██      ██  ██\n'
        '██████      ██████\n'
        '██████████████████\n'
        '██  ████  ████  ██\n'
        '██████████████████'
    )
