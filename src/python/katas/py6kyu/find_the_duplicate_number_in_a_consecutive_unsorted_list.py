"""Kata url: https://www.codewars.com/kata/558f0553803bc3c4720000af."""

from collections import Counter

def find_dup(arr):
    return next((k for k, v in Counter(arr).items() if v > 1), 0)