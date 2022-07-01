"""Kata url: https://www.codewars.com/kata/520b9d2ad5c005041100000f."""


def pig_it(text):
    return ' '.join(
        (w[1:] + w[0] + 'ay') if w.isalpha() else w
        for w in text.split(' ')
    )


def test_pig_it():
    assert pig_it('Pig latin is cool') == 'igPay atinlay siay oolcay'
    assert pig_it('This is my string') == 'hisTay siay ymay tringsay'
