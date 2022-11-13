"""Kata url: https://www.codewars.com/kata/53f40dff5f9d31b813000774."""
from collections import defaultdict


def recover_secret(triplets) -> str:
    data = defaultdict(int)

    for i in range(len(triplets)):
        for a, b, c in triplets:

            if data[a] >= data[b]:
                data[a], data[b] = data[b], data[b] + 1

            if data[b] >= data[c]:
                data[b], data[c] = data[c], data[c] + 1

    return ''.join(sorted(data.keys(), key=data.get))


def test_recover_string():
    assert recover_secret(
        [
            ['t', 'u', 'p'],
            ['w', 'h', 'i'],
            ['t', 's', 'u'],
            ['a', 't', 's'],
            ['h', 'a', 'p'],
            ['t', 'i', 's'],
            ['w', 'h', 's']
        ]
    ) == "whatisup"
