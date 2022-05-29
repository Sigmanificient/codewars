"""Kata url: https://www.codewars.com/kata/54da5a58ea159efa38000836."""

def find_it(seq):
    return [x for x in set(seq) if seq.count(x) % 2][-1]
