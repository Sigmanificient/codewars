"""Kata url: https://www.codewars.com/kata/586d6cefbcc21eed7a001155."""


def longest_repetition(chars):
    if not chars:
        return '', 0

    occurrences = []
    p, count = '', 1
    for c in chars:
        if c == p:
            count += 1
        elif p:
            occurrences.append((p, count))
            count = 1
        p = c

    occurrences.append((p, count))
    return max(occurrences, key=lambda t: t[1])


def test_longest_repetition():
    assert longest_repetition("aaaabb") == ('a', 4)
    assert longest_repetition("bbbaaabaaaa") == ('a', 4)
    assert longest_repetition("cbdeuuu900") == ('u', 3)
    assert longest_repetition("abbbbb") == ('b', 5)
    assert longest_repetition("aabb") == ('a', 2)
    assert longest_repetition("ba") == ('b', 1)
    assert longest_repetition("") == ('', 0)
