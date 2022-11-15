"""Kata url: https://www.codewars.com/kata/5768a693a3205e1cc100071f."""


def initialize_names(name):
    if ' ' not in name:
        return name

    first, *middle, last = name.split(' ')
    if not middle:
        return name

    m = ' '.join(f'{m[0]}.' for m in middle)
    return f"{first} {m} {last}"


def test_initialize_name():
    assert initialize_names('Jack Ryan') == 'Jack Ryan'
    assert initialize_names('Lois Mary Lane') == 'Lois M. Lane'
    assert initialize_names('Dimitri') == 'Dimitri'
    assert initialize_names(
        'Alice Betty Catherine Davis'
    ) == 'Alice B. C. Davis'
