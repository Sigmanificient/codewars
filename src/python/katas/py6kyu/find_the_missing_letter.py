from typing import List


def find_missing_letter(chars: List[str]) -> str:
    print(chars)

    charset = 'abcdefghijklmnopqrstuvwxyz'
    chars = ''.join(chars)
    if chars.isupper():
        charset = charset.upper()

    for a, b in zip(charset[charset.index(chars[0]):], chars):
        if a != b:
            return a


def test_find_missing_letter():
    assert find_missing_letter(['a', 'b', 'c', 'd', 'f']) == 'e'
    assert find_missing_letter(['A', 'B', 'C', 'D', 'F']) == 'E'

    assert find_missing_letter(['O', 'Q', 'R', 'S']) == 'P'
    assert find_missing_letter(['V', 'X', 'Y', 'Z']) == 'W'
