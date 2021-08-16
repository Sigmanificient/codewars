"""Kata url: https://www.codewars.com/kata/5650ab06d11d675371000003."""


def split_in_parts(s: str, part_length: int) -> str:
    return ' '.join(s[i:i + part_length] for i in range(0, len(s), part_length))
