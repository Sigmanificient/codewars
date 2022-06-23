"""Kata url: https://www.codewars.com/kata/514a7ac1a33775cbb500001e."""

from typing import Dict


def mystery() -> Dict[str, str]:
    return {'sanity': 'Hello'}


def test_mystery():
    assert mystery() == {'sanity': 'Hello'}, 'Mystery has not returned to sanity'
