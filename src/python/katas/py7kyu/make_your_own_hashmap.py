"""Kata url: https://www.codewars.com/kata/5a6a02adcadebf618400002b."""
from collections import defaultdict
from typing import DefaultDict, Dict, List


def my_hash_map(list_of_strings: List[str]) -> Dict[int, List[str]]:
    out: DefaultDict[int, List[str]] = defaultdict(list)
    for string in list_of_strings:
        out[sum(map(ord, string))].append(string)

    return dict(out)


def test_my_hash_map():
    list_of_strings = ["alphabet"]
    assert my_hash_map(list_of_strings) == {833: ["alphabet"]}

    list_of_strings.append("black")
    assert my_hash_map(list_of_strings) == {833: ["alphabet"], 509: ["black"]}
