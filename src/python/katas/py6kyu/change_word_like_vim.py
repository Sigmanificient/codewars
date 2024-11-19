"""Kata url: https://www.codewars.com/kata/668d005814d24222662d06fb."""
from string import ascii_letters, digits

BASIC_WORD = ascii_letters + digits + '_'


def get_word_type(c):
    return ((c in BASIC_WORD) << 1) | (c.isspace())

def change_word(text: str, index: int, new_word: str) -> str:
    word_type = get_word_type(text[index])

    while index >= 1 and get_word_type(text[index]) == word_type:
        index -= 1
    if get_word_type(text[index]) != word_type:
        index += 1

    cut = index
    while cut < (len(text) - 1) and get_word_type(text[cut]) == word_type:
        cut += 1
    if get_word_type(text[cut]) != word_type:
        cut -= 1

    return text[:index] + new_word + text[cut + 1:]