"""Kata: https://www.codewars.com/kata/5782b5ad202c0ef42f0012cb."""
from string import ascii_lowercase, ascii_uppercase, digits

_PUNCTUATIONS: str = ".,:;-?! '()$%&\""
REGION: str = (
    ascii_uppercase
    + ascii_lowercase
    + digits
    + _PUNCTUATIONS
)

REGION_MIRROR = REGION[::-1]
REGION_INDEXES = {i: c for c, i in enumerate(REGION)}


def encrypt(text: str) -> str:
    if not text:
        return text

    if any(c not in REGION for c in text):
        raise ValueError

    case_swapped = ''.join(
        c.swapcase() if i & 1 else c for i, c in enumerate(text)
    )

    return (
        REGION_MIRROR[REGION_INDEXES[case_swapped[0]]]
        + ''.join(
            REGION[(REGION_INDEXES[c] - REGION_INDEXES[c2])]
            for c, c2 in zip(case_swapped, case_swapped[1:])
        )
    )


def decrypt(encrypted_text: str) -> str:
    if not encrypted_text:
        return encrypted_text

    if any(c not in REGION for c in encrypted_text):
        raise ValueError

    text = REGION_MIRROR[REGION_INDEXES[encrypted_text[0]]]
    for i, c in enumerate(encrypted_text[1::]):
        text += REGION[(REGION_INDEXES[text[i]] - REGION_INDEXES[c]) % 77]

    return ''.join(
        c.swapcase() if i & 1 else c for i, c in enumerate(text)
    )


def test_encrypt_2i_diff():
    assert encrypt("") == ""

    assert encrypt("Business") == "&61kujla"
    assert encrypt("This is a test!") == "5MyQa9p0riYplZc"

    assert encrypt(
        "Do the kata \"Kobayashi-Maru-Test!\" Endless fun and excitement when"
        " finding a solution!"
    ) == (
        "$-Wy,dM79H'i'o$n0C&I.ZTcMJw5vPlZc Hn!krhlaa:khV mkL;gvtP-S7Rt1Vp2RV:wV"
        "9VuhO Iz3dqb.U0w"
    )

    assert (
        encrypt("This kata is very interesting!")
        == "5MyQa79H'ijQaw!Ns6jVtpmnlZ.V6p"
    )


def test_decrypt_2i_diff():
    assert decrypt("") == ""
    assert decrypt(
        "$-Wy,dM79H'i'o$n0C&I.ZTcMJw5vPlZc Hn!krhlaa:khV mkL;gvtP-S7Rt1Vp2RV:wV"
        "9VuhO Iz3dqb.U0w"
    ) == (
        "Do the kata \"Kobayashi-Maru-Test!\" Endless fun and excitement when"
        " finding a solution!"
    )

    assert decrypt("5MyQa9p0riYplZc") == "This is a test!"
    assert (
        decrypt("5MyQa79H'ijQaw!Ns6jVtpmnlZ.V6p")
        == "This kata is very interesting!"
    )
