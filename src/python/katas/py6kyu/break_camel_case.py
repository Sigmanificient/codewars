"""Kata url: https://www.codewars.com/kata/5208f99aee097e6552000148"""


def solution(s: str) -> str:
    return ''.join(c if c.islower() else f' {c}' for c in s)


def test_solution():
    assert solution("helloWorld") == "hello World"
    assert solution("camelCase") == "camel Case"
    assert solution("breakCamelCase") == "break Camel Case"
