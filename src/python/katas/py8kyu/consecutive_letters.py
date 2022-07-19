"""Kata url: https://www.codewars.com/kata/5ce6728c939bf80029988b57."""

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def solve(st):
    seq = sorted(set(st))
    if len(seq) != len(st):
        return False

    i = alphabet.index(min(seq))
    return all(
        alphabet[i + c] == l
        for c, l in enumerate(seq[1:], start=1)
    )
