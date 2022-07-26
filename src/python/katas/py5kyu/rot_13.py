"""Kata url: https://www.codewars.com/kata/530e15517bc88ac656000716."""


def rot13(message: str) -> str:
    charset = "abcdefghijklmnopqrstuvwxyz"

    buff = []
    for char in message:
        if (l := char.lower()) not in charset:
            buff.append(char)
            continue

        n_char = charset[(charset.index(l) + 13) % 26]

        if char.isupper():
            n_char = n_char.upper()

        buff.append(n_char)

    return "".join(buff)


def test_rot13():
    assert rot13("test") == "grfg"
    assert rot13("Test") == "Grfg"
    assert rot13("Codewars") == "Pbqrjnef"

    assert rot13("Hello world!") == "Uryyb jbeyq!"
