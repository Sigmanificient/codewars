"""Kata url: https://www.codewars.com/kata/597754ba62f8a19c98000030."""


def vowel_change(txt: str, vow: str) -> str:
    return txt.translate(str.maketrans("aeiou", vow * 5))


def test_vowel_change():
    assert (
        vowel_change(
            "hannah hannah bo-bannah banana fanna fo-fannah fee, fy, mo-mannah. hannah!",
            "i",
        )
        == "hinnih hinnih bi-binnih binini finni fi-finnih fii, fy, mi-minnih. hinnih!"
    )
    assert (
        vowel_change("adira wants to go to the park", "o")
        == "odoro wonts to go to tho pork"
    )
