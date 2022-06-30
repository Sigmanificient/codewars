# Kata url: https://www.codewars.com/kata/545991b4cbae2a5fda000158.
from typing import Any, List


def include(arr: List[Any], item: Any) -> bool:
    return item in arr


def test_include():
    assert include([1, 2, 3, 4], 3)
    assert not include([1, 2, 4, 5], 3)
