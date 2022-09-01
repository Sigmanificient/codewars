"""Kata url: https://www.codewars.com/kata/59c5f4e9d751df43cf000035."""
VOWELS = set('aeiou')


def solve(s):
    count = 0
    mx = 0

    for ch in s:
        if ch in VOWELS:
            count += 1
            continue

        elif count > mx:
            mx = count

        count = 0

    return mx


def test_solve():
    assert solve("codewarriors") == 2
    assert solve("suoidea") == 3
    assert solve("ultrarevolutionariees") == 3
    assert solve("strengthlessnesses") == 1
    assert solve("cuboideonavicuare") == 2
    assert solve("chrononhotonthuooaos") == 5
    assert solve("iiihoovaeaaaoougjyaw") == 8
