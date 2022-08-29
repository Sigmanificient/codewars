"""Kata url: https://www.codewars.com/kata/5f7c38eb54307c002a2b8cc8."""


def remove_parentheses(s):
    level = 0
    out = ''

    for char in s:
        if char == '(':
            level += 1
            continue

        if char == ')':
            level -= 1
            continue

        if not level:
            out += char

    return out


def test_remove_parentheses():
    assert remove_parentheses("example(unwanted thing)example") == "exampleexample"
    assert remove_parentheses("example (unwanted thing) example") == "example  example"
    assert remove_parentheses("a (bc d)e") == "a e"
    assert remove_parentheses("a(b(c))") == "a"
    assert remove_parentheses("hello example (words(more words) here) something") == "hello example  something"
    assert remove_parentheses("(first group) (second group) (third group)") == "  "
