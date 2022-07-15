"""Kata url: https://www.codewars.com/kata/52b757663a95b11b3d00062d."""


def to_weird_case(string):
    return ' '.join(
        ''.join(
            char.lower() if c % 2 else char.upper()
            for c, char in enumerate(w)
        ) for w in string.split(' ')
    )


def test_to_weird_case():
    assert to_weird_case('This') == 'ThIs'
    assert to_weird_case('is') == 'Is'
    assert to_weird_case('This is a test') == 'ThIs Is A TeSt'
