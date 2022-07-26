"""Kata url: https://www.codewars.com/kata/57cff961eca260b71900008f."""


from typing import Union, List


def is_vow(inp: List[Union[int, str]]) -> List[Union[int, str]]:
    buf: List[Union[int, str]] = []
    for x in inp:
        letter: str = chr(x) if isinstance(x, int) else x

        if letter in "aeiou":
            buf.append(letter)

        else:
            buf.append(x)

    return buf


def test_is_vow():
    tests = (
        (
            [
                118,
                "u",
                120,
                121,
                "u",
                98,
                122,
                "a",
                120,
                106,
                104,
                116,
                113,
                114,
                113,
                120,
                106,
            ],
            [
                118,
                117,
                120,
                121,
                117,
                98,
                122,
                97,
                120,
                106,
                104,
                116,
                113,
                114,
                113,
                120,
                106,
            ],
        ),
        (
            ["e", 121, 110, 113, 113, 103, 121, 121, "e", 107, 103],
            [101, 121, 110, 113, 113, 103, 121, 121, 101, 107, 103],
        ),
        ([118, 103, 110, 109, 104, 106], [118, 103, 110, 109, 104, 106]),
        (
            [107, 99, 110, 107, 118, 106, 112, 102],
            [107, 99, 110, 107, 118, 106, 112, 102],
        ),
        ([100, 100, 116, "i", "u", 121], [100, 100, 116, 105, 117, 121]),
    )

    for exp, inp in tests:
        assert is_vow(inp) == exp
