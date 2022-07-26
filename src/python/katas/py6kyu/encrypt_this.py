"""Kata url: https://www.codewars.com/kata/5848565e273af816fb000449."""


def encrypt_this(text: str) -> str:
    buff = ""
    for w in text.split():
        for c, char in enumerate(w, start=1):
            if c == 1:
                buff += f"{ord(char)}"

            elif c == 2:
                buff += w[-1]

            elif c == len(w):
                buff += w[1]

            else:
                buff += char

        buff += " "
    return buff[:-1]


def test_encrypt_this():
    assert encrypt_this("") == ""
    assert (
        encrypt_this("A wise old owl lived in an oak")
        == "65 119esi 111dl 111lw 108dvei 105n 97n 111ka"
    )
    assert (
        encrypt_this("The more he saw the less he spoke")
        == "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"
    )
    assert (
        encrypt_this("The less he spoke the more he heard")
        == "84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"
    )
    assert (
        encrypt_this("Why can we not all be like that wise old bird")
        == "87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri"
    )
    assert (
        encrypt_this("Thank you Piotr for all your help")
        == "84kanh 121uo 80roti 102ro 97ll 121ruo 104ple"
    )
