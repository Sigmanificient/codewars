"""Kata url: https://www.codewars.com/kata/59cfc000aeb2844d16000075."""


def capitalize(s: str) -> str:
    x = ''.join(
        char.upper() if c % 2 else char.lower()
        for c, char in enumerate(s)
    )

    return [x.swapcase(), x]


def test_capitalize():
    assert capitalize("") == ['', '']
    assert capitalize("abcdef") == ['AbCdEf', 'aBcDeF']
    assert capitalize("codewars") == ['CoDeWaRs', 'cOdEwArS']
    assert capitalize("abracadabra") == ['AbRaCaDaBrA', 'aBrAcAdAbRa']
    assert capitalize("codewarriors") == ['CoDeWaRrIoRs', 'cOdEwArRiOrS']
