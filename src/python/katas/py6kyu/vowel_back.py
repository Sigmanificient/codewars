"""Kata url: https://www.codewars.com/kata/57cfd92c05c1864df2001563."""
from string import ascii_lowercase as chars
from typing import Dict

vowels = set('aeiou')
special: Dict[str, int] = {'c': -1, 'o': -1, 'd': -3, 'e': -4}


def vowel_back(st: str) -> str:
    encoded = ''

    for char in st:
        move = special.get(char, 0)
        if not move:
            move = -5 if char in vowels else 9

        out = chars[(chars.index(char) + move) % 26]

        print(out)
        if out in special.keys():
            out = char

        encoded += out

    return encoded


def test_vowel_back():
    assert vowel_back("testcase") == "tabtbvba"
    assert vowel_back("codewars") == "bnaafvab"
    assert vowel_back("exampletesthere") == "agvvyuatabtqaaa"
    assert vowel_back("returnofthespacecamel") == "aatpawnftqabyvbabvvau"
    assert vowel_back("bringonthebootcamp") == "kaiwpnwtqaknntbvvy"
    assert vowel_back("weneedanofficedog") == "fawaaavwnffibaanp"
