def rot13(message):
    charset = 'abcdefghijklmnopqrstuvwxyz'

    buff = []
    for char in message:
        if (l := char.lower()) not in charset:
            buff.append(char)
            continue

        n_char = charset[(charset.index(l) + 13) % 26]

        if char.isupper():
            n_char = n_char.upper()

        buff.append(n_char)

    return ''.join(buff)


def test_rot13():
    assert rot13("test") == "grfg"
    assert rot13("Test") == "Grfg"
    assert rot13("Codewars") == "Pbqrjnef"
