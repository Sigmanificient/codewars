"""Kata url: https://www.codewars.com/kata/54cf7f926b85dcc4e2000d9d."""
from __future__ import annotations

from collections import Counter


class Node:

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def frequencies(s):
    return list(Counter(s).items())


def build_tree(freqs):
    freqs = sorted(freqs, key=lambda x: x[1], reverse=True)

    while len(freqs) > 1:
        k_1, v_1 = freqs.pop()
        k_2, v_2 = freqs.pop()

        node = Node(k_1, k_2)
        freqs.append([node, v_1 + v_2])
        freqs = sorted(freqs, key=lambda x: x[1], reverse=True)

    return freqs[0][0]


def retrieve_codes(node, code=''):
    if isinstance(node, str):
        return {node: code}

    return (
        retrieve_codes(node.left, code + '0')
        | retrieve_codes(node.right, code + '1')
    )


def encode(freqs, s):
    if not freqs or len(freqs) < 2:
        return None
    if not s:
        return ''

    codes = retrieve_codes(build_tree(freqs))
    return ''.join(codes[c] for c in s)


def decode(freqs, bits):
    if not freqs or len(freqs) < 2:
        return None
    if not bits:
        return ''

    codes = {v: k for k, v in retrieve_codes(build_tree(freqs)).items()}
    collect = out = ''

    for b in bits:
        collect += b

        if codes.get(collect):
            out += codes[collect]
            collect = ''
    return out
