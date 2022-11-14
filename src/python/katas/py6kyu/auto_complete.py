"""Kata url: https://www.codewars.com/kata/5389864ec72ce03383000484."""
from string import ascii_lowercase


def autocomplete(input_, dictionary):
    i = ''.join(x for x in input_ if x in ascii_lowercase)
    return [word for word in dictionary if word.lower().startswith(i)][:5]


def test_autocomplete():
    dictionary = [
        'abnormal', 'arm-wrestling', 'absolute', 'airplane',
        'airport', 'amazing', 'apple', 'ball'
    ]

    assert autocomplete('ai', dictionary) == ['airplane', 'airport']
    assert autocomplete('a', dictionary) == [
        'abnormal', 'arm-wrestling', 'absolute', 'airplane', 'airport'
    ]
