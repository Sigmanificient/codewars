# Kata url: https://www.codewars.com/kata/570597e258b58f6edc00230d.
from typing import Optional


def array(string: str) -> Optional[str]:
    return ' '.join(string.split(',')[1:-1]) or None
