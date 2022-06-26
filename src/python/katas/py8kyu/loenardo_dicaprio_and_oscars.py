"""Kata url: https://www.codewars.com/kata/56d49587df52101de70011e4."""


def leo(oscar: int) -> str:
    if oscar == 88:
        return "Leo finally won the oscar! Leo is happy"

    if oscar == 86:
        return "Not even for Wolf of wallstreet?!"

    if oscar < 88:
        return "When will you give Leo an Oscar?"

    return "Leo got one already!"


def test_leo():
    assert leo(89) == "Leo got one already!"
    assert leo(88) == "Leo finally won the oscar! Leo is happy"
    assert leo(87) == "When will you give Leo an Oscar?"
    assert leo(86) == "Not even for Wolf of wallstreet?!"
