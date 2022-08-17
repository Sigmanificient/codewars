"""Kata url: https://www.codewars.com/kata/59a96d71dbe3b06c0200009c."""


def generate_shape(n: int) -> str:
    return '\n'.join('+' * n for _ in range(n))


def test_generate_shape():
    assert generate_shape(0) == ''
    assert generate_shape(1) == '+'

    assert generate_shape(3) == '+++\n+++\n+++'
    assert generate_shape(8) == (
        '++++++++\n++++++++\n++++++++\n++++++++'
        '\n++++++++\n++++++++\n++++++++\n++++++++'
    )
