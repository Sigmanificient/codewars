"""Kata url: https://www.codewars.com/kata/5202ef17a402dd033c000009."""


def title_case(title: str, minor_words: str = '') -> str:
    minor_wl = tuple(map(str.lower, minor_words.split(' ')))
    return ' '.join(
        word.lower() if (c and word.lower() in minor_wl) else word.capitalize()
        for c, word in enumerate(title.split(' '))
    )


def test_title_case():
    assert title_case('') == ''
    assert title_case('a clash of KINGS', 'a an the of') == 'A Clash of Kings'
    assert title_case('THE WIND IN THE WILLOWS', 'The In') == 'The Wind in the Willows'
    assert title_case('the quick brown fox') == 'The Quick Brown Fox'
