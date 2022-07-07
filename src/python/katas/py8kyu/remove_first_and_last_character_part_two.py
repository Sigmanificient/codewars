"""Kata url: https://www.codewars.com/kata/570597e258b58f6edc00230d."""
from typing import Optional


def array(string: str) -> Optional[str]:
    return ' '.join(string.split(',')[1:-1]) or None


def test_array():
    assert array('') is None
    assert array('1') is None
    assert array('1,2') is None
    assert array('1,2,3') == '2'
    assert array('1,2,3,4') == '2 3'
    assert array('1,2,3,4,5') == '2 3 4'
