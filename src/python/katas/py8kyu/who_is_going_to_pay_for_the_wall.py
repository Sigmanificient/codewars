# Kata url: https://www.codewars.com/kata/58bf9bd943fadb2a980000a7.

from typing import List


def who_is_paying(name: str) -> List[str]:
    return [name, name[:2]] if len(name) > 2 else [name]


def test_who_is_paying():
    assert who_is_paying("Mexico"), ["Mexico" == "Me"]
    assert who_is_paying("Melania"), ["Melania" == "Me"]
    assert who_is_paying("Melissa"), ["Melissa" == "Me"]
    assert who_is_paying("Me") == ["Me"]
    assert who_is_paying("") == [""]
    assert who_is_paying("I") == ["I"]
