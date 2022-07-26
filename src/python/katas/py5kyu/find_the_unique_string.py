"""Kata url: https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3."""
from typing import List


def find_uniq(arr: List[str]) -> str:
    k, hash_word = {}, []

    for word in arr:
        s = "".join(sorted(set(word.lower())))
        hash_word.append(s)
        k[s] = word

    return k[min(k.keys(), key=hash_word[:3].count)]


def test_find_uniq():
    assert find_uniq(["Aa", "aaa", "aaaaa", "BbBb", "Aaaa", "AaAaAa", "a"]) == "BbBb"
    assert find_uniq(["abc", "acb", "bac", "foo", "bca", "cab", "cba"]) == "foo"
    assert find_uniq(["    ", "a", "  "]) == "a"
