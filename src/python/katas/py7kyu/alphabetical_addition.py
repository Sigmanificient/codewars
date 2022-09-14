"""Kata url: https://www.codewars.com/kata/5d50e3914861a500121e1958/."""


def add_letters(*letters):
    ascii_offset = ord('a') - 1
    total = sum(ord(char) - ascii_offset for char in letters)
    return chr(ascii_offset + ((total % 26) or 26))


def test_add_letters():
    assert add_letters('a', 'b', 'c') == 'f'
    assert add_letters('z') == 'z'
    assert add_letters('a', 'b') == 'c'
    assert add_letters('c') == 'c'
    assert add_letters('z', 'a') == 'f'
    assert add_letters('a', 'b', 'c') == 'a'
    assert add_letters('y', 'c', 'b') == 'd'
    assert add_letters() == 'z'
