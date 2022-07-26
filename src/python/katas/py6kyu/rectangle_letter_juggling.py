"""Kata url: https://www.codewars.com/kata/60d6f2653cbec40007c92755."""


from math import sqrt, ceil


def cipher_text(plain_text: str) -> str:
    normalized = "".join(c for c in plain_text.lower() if c.isalpha())
    if not normalized:
        return ""

    l = len(normalized)
    b = ceil(sqrt(l))

    rect = [normalized[i : i + b] for i in range(0, l, b)]
    rect[-1] = rect[-1].ljust(b, " ")

    print(normalized)
    print(rect)

    return " ".join("".join(line) for line in zip(*rect))


def test_cipher_text():
    assert cipher_text(
        "When nobody is around, the trees gossip about the people who have walk"
        "ed under them."
    ) == (
        "wytotear hihstwlt eseshhkh natieoee nrrpphdm ooeaeau  buebovn  onsoped"
        "  ddgulwe "
    )

    assert (
        cipher_text("I want a giraffe, but I'm a turtle eating waffles.")
        == "iiuril wrttne aailgs nfmew  tfaea  aetaf  gbutf "
    )

    assert cipher_text(
        "Dolores wouldn't have eaten the meal if she had known what it actuall" "y was."
    ) == ("dovhsoty oueehwaw llemenca odaehwts rntaahu  eteldaa  shniktl  watfnil" " ")

    assert (
        cipher_text("She says she has the ability to hear the soundtrack of your life.")
        == "shaoscl hebhoki ehieuof salanfe asirdy  ytttto  shyhru  setear "
    )

    assert (
        cipher_text("I've always wanted to go to Tajikistan, but my cat would miss me.")
        == "isoiuom vwgktue eaoiml  antsyd  ltotcm  wetaai  adants  ytjbws "
    )

    assert cipher_text("###") == ""
