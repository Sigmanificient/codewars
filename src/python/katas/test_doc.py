import re
import os


def check_doc(filename):
    with open(filename) as f:
        return re.fullmatch(
            r'^"""Kata url: https://www.codewars.com/kata/(.*)"""$',
            next(f)
        )


def test_doc():
    for kyu_lvl in range(3, 9):
        kata_dir = f'src/python/katas/py{kyu_lvl}kyu'
        for filename in os.listdir(kata_dir):
            if not filename.endswith('.py'):
                continue

            assert check_doc(f'{kata_dir}/{filename}'), f'{filename} have no doc'
