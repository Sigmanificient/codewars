"""Kata url: https://www.codewars.com/kata/56541980fa08ab47a0000040."""


def printer_errors(s: str) -> str:
    return f"{sum(c not in 'abcdefghijklm' for c in s)}/{len(s)}"


def test_printer_errors():
    assert (
        printer_errors("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz")
        == "3/56"
    )
    assert printer_errors("kkkmmmllllpppp") == "4/14"
    assert printer_errors("") == "0/0"
