"""Kata url: https://www.codewars.com/kata/51b62bf6a9c58071c600001b."""
romans = {
    'M': 1_000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}

successors = ''.join(romans)

def solution(n):
    out = []

    for idx, (k, v) in enumerate(romans.items()):
        count = 0
        while n >= v:
            n -= v
            count += 1

        if count <= 3:
            out.extend(k * count)
            continue

        s = successors[idx-1]

        if out and out[-1] == s:
            s = successors[idx-2]
            out.pop()

        out.extend(k + s)

    return ''.join(out)