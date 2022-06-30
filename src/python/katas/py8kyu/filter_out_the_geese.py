"""Kata url: https://www.codewars.com/kata/57ee4a67108d3fd9eb0000e7."""

from typing import List

geese: List[str] = [
    "African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"
]


def goose_filter(birds: List[str]) -> List[str]:
    return [bird for bird in birds if bird not in geese]


def test_goose_filter():
    assert goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]) == ["Mallard", "Hook Bill", "Crested", "Blue Swedish"]
    assert goose_filter(["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"]) == ["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"]
    assert goose_filter(["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]) == []
