"""Kata url: https://www.codewars.com/kata/5254ca2719453dcc0b00027d."""
from itertools import permutations as p
from typing import List


def permutations(string: str) -> List[str]:
    return list({''.join(string) for string in p(string)})


def test_permutations():
    assert sorted(permutations('a')) == ['a']
    assert sorted(permutations('ab')) == ['ab', 'ba']
    assert sorted(permutations('aabb')) == ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
