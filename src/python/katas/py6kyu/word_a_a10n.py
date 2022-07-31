"""Kata url: https://www.codewars.com/kata/5375f921003bf62192000746."""


def abbreviate(s: str) -> str:
    out = word = ""
    m = len(s)

    for c, char in enumerate(f"{s}."):
        if char.isalpha():
            word += char
            continue

        if len(word) > 3:
            word = f"{word[0]}{len(word) - 2}{word[-1]}"

        out += word
        if c != m:
            out += char

        word = ""

    return out


def test_abbreviate():
    assert abbreviate("internationalization") == "i18n"
    assert abbreviate("accessibility") == "a11y"
    assert abbreviate("Accessibility") == "A11y"
    assert abbreviate("elephant-ride") == "e6t-r2e"
