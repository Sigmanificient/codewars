"""Kata url: https://www.codewars.com/kata/56a5d994ac971f1ac500003e."""

from typing import List


def longest_consec(strarr: List[str], k: int) -> str:
    if k < 0 or k > len(strarr):
        return ''

    lengths = [len(x) for x in strarr]

    total = index = 0

    for i in range(len(strarr) - k + 1):
        t = sum(lengths[i:i + k])

        if t > total:
            total = t
            index = i

    return ''.join(strarr[index:index + k])


def test_longest_consec():
    assert longest_consec(
        ["zone", "abigail", "theta", "form", "libe", "zas"], 2
    ) == "abigailtheta"

    assert longest_consec(
        [
            "ejjjjmmtthh",
            "zxxuueeg",
            "aanlljrrrxx",
            "dqqqaaabbb",
            "oocccffuucccjjjkkkjyyyeehh"
        ], 1
    ) == "oocccffuucccjjjkkkjyyyeehh"

    assert longest_consec([], 3) == ""
    assert longest_consec(
        [
            "itvayloxrp",
            "wkppqsztdkmvcuwvereiupccauycnjutlv",
            "vweqilsfytihvrzlaodfixoyxvyuyvgpck"
        ], 2
    ) == "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck"

    assert longest_consec(
        ["wlwsasphmxx", "owiaxujylentrklctozmymu", "wpgozvxxiu"], 2
    ) == "wlwsasphmxxowiaxujylentrklctozmymu"

    assert longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2) == ""
    assert longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 3) == "ixoyx3452zzzzzzzzzzzz"
    assert longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 15) == ""
    assert longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 0) == ""
