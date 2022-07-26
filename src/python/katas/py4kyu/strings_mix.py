"""Kata url: https://www.codewars.com/kata/5629db57620258aa9d000014."""

from collections import Counter
from string import ascii_lowercase


def mix(s1: str, s2: str) -> str:
    c1, c2 = Counter(s1), Counter(s2)
    keys = set(c1).union(c2)
    out, max_ = [], 0

    for key in keys:
        if key not in ascii_lowercase:
            continue

        v1, v2 = c1[key], c2[key]
        if (m := max(v1, v2)) > max_:
            max_ = m

        if m < 2:
            continue

        out.append(f'{"=" if v1 == v2 else 1 + (m == v2)}:{key * m}')

    return "/".join(sorted(out, key=lambda x: f"{max_ - x.count(x[-1])}{x[0]}{x[-1]}"))


def test_mix():
    assert mix("Are they here", "yes, they are here") == "2:eeeee/2:yy/=:hh/=:rr"

    assert (
        mix("Sadus:cpms>orqn3zecwGvnznSgacs", "MynwdKizfd$lvse+gnbaGydxyXzayp")
        == "2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz"
    )

    assert (
        mix("looping is fun but dangerous", "less dangerous than coding")
        == "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg"
    )
    assert (
        mix(" In many languages", " there's a pair of functions")
        == "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt"
    )
    assert mix("Lords of the Fallen", "gamekult") == "1:ee/1:ll/1:oo"
    assert mix("codewars", "codewars") == ""
    assert (
        mix("A generation must confront the looming ", "codewarrs")
        == "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr"
    )
