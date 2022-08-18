"""Kata url: https://www.codewars.com/kata/5803a6d8db07c59fff00015f."""


def starts_with(st: str, prefix: str) -> bool:
    return st.startswith(prefix)


def test_starts_with():
    assert starts_with("hello world!", "hello")
    assert not starts_with("hello world!", "HELLO")
    assert not starts_with("nowai", "nowaisir")

    assert starts_with("", "")
    assert starts_with("abc", "")
    assert not starts_with("", "abc")
