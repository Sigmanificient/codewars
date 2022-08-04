"""Kata url: https://www.codewars.com/kata/5569b10074fe4a6715000054."""
from collections import Counter
from typing import Dict, List


def count(array: List[str]) -> Dict[str, int]:
    return dict(Counter(array))


def test_count():
    assert count([]) == {}
    assert count(['a']), {'a': 1}
    assert count(['a', 'a', 'b', 'b', 'b']) == {'a': 2, 'b': 3}
    assert count(['a', 'b', 'b', 'b', 'a']) == {'a': 2, 'b': 3}
    assert count(
        ["", 'a', True, 15, "b", "b"]
    ) == {'': 1, 'a': 1, 15: 1, 'b': 2, True: 1}
