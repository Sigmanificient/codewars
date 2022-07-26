"""Kata url: https://www.codewars.com/kata/52aeb2f3ad0e952f560005d3."""


def sort_gift_code(code: str) -> str:
    return ''.join(sorted(code))


def test_sort_gift_code():
    assert sort_gift_code('abcdef') == 'abcdef'
    assert sort_gift_code('pqksuvy') == 'kpqsuvy'
    assert sort_gift_code(
        'zyxwvutsrqponmlkjihgfedcba'
    ) == 'abcdefghijklmnopqrstuvwxyz'
