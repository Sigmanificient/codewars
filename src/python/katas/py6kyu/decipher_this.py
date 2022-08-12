"""Kata url: https://www.codewars.com/kata/581e014b55f2c52bb00000f8."""


def decipher_this(string: str) -> str:
    out = []

    for word in string.split(' '):
        m = len(word)

        i = 0
        while i < m and word[i].isdigit():
            i += 1

        first_letter = chr(int(word[:i]))
        word = word[i:]

        if len(word) >= 2:
            word = word[-1] + word[1:-1] + word[0]

        out.append(f'{first_letter}{word}')

    return ' '.join(out)


def test_decipher_this():
    assert decipher_this(
        "65 119esi 111dl 111lw 108dvei 105n 97n 111ka"
    ) == "A wise old owl lived in an oak"

    assert decipher_this(
        "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"
    ) == "The more he saw the less he spoke"

    assert decipher_this(
        "84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"
    ) == "The less he spoke the more he heard"

    assert decipher_this(
        "87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri"
    ) == "Why can we not all be like that wise old bird"

    assert decipher_this(
        "84kanh 121uo 80roti 102ro 97ll 121ruo 104ple"
    ) == "Thank you Piotr for all your help"
