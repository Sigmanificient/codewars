"""Kata url: https://www.codewars.com/kata/511f0fe64ae8683297000001."""
from typing import List

websites: List[str] = globals().get('websites', [])
websites.append("codewars")


def test_solution():
    websites_internal = ['codewars']
    assert websites_internal == websites
    assert len(websites) == 1
    assert websites_internal[0] == 'codewars'
