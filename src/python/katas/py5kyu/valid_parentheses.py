"""Kata url: https://www.codewars.com/kata/52774a314c2333f0a7000688."""


def valid_parentheses(string: str) -> bool:
    depth = 0

    for ch in string:
        if ch == '(':
            depth += 1
        elif ch == ')':
            depth -= 1

        if depth < 0:
            return False

    return depth == 0


def test_valid_parentheses():
    assert valid_parentheses("")
    assert valid_parentheses("hi(hi)()")
    assert not valid_parentheses("  (")
    assert not valid_parentheses(")test")
    assert not valid_parentheses("hi())(")
