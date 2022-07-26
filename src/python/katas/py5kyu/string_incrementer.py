"""Kata url: https://www.codewars.com/kata/54a91a4883a7de5d7800009c."""


def increment_string(string: str) -> str:
    i = 0
    while i < len(string) and string[-(i + 1)].isdigit():
        i += 1

    if not i:
        return f"{string}1"

    return f"{string[:-i]}{int(string[-i:]) + 1:0{i}}"


def test_increment_string():
    assert increment_string("foo") == "foo1"
    assert increment_string("foobar001") == "foobar002"
    assert increment_string("foobar1") == "foobar2"
    assert increment_string("foobar00") == "foobar01"
    assert increment_string("foobar99") == "foobar100"
    assert increment_string("foobar099") == "foobar100"
    assert increment_string("") == "1"
