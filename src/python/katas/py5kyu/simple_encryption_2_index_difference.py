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


if __name__ == '__main__':
    print(decrypt(encrypt("Business")))
