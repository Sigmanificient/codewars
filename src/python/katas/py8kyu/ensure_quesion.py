"""Kata url: https://www.codewars.com/kata/5866fc43395d9138a7000006."""


def ensure_question(s: str) -> str:
    return s if s.endswith("?") else f"{s}?"


def test_ensure_question():
    assert ensure_question("") == "?", "Expected: '?'"
    assert ensure_question("Yes") == "Yes?", "Expected: '?'"
    assert ensure_question("No?") == "No?", "Expected: '?'"
    assert ensure_question("Well????") == "Well????", "Expected: '?'"
