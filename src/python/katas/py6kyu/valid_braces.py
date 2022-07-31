"""Kata url: https://www.codewars.com/kata/5277c8a221e209d3f6000b56."""


def valid_braces(string: str) -> bool:
    braces = "[](){}"
    stack = [0]

    for item in string:
        index = braces.index(item)

        if not index % 2:
            stack.append(index)
            continue

        if index - 1 != stack.pop():
            return False

    return len(stack) == 1


def test_valid_braces():
    assert valid_braces("()")
    assert not valid_braces("(}")
    assert valid_braces("[]")
    assert not valid_braces("[(])")
    assert valid_braces("{}")
    assert valid_braces("{}()[]")
    assert valid_braces("([{}])")
    assert not valid_braces("([}{])")
    assert valid_braces("{}({})[]")
    assert valid_braces("(({{[[]]}}))")
    assert not valid_braces("(((({{")
    assert not valid_braces(")(}{][")
    assert not valid_braces("())({}}{()][][")
