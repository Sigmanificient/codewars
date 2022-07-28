"""Kata url: https://www.codewars.com/kata/57fcaed83206fb15fd00027a."""


def replace_nth(text: str, n: int, old_value: str, new_value: str) -> str:
    if n <= 0:
        return text

    out = ""
    c = 0

    for char in text:
        if char == old_value:
            c += 1

            if not c % n:
                char = new_value

        out += char

    return out


def test_replace_nth():
    assert (
        replace_nth("Vader said: No, I am your father!", 2, "a", "o")
        == "Vader soid: No, I am your fother!"
    )

    assert (
        replace_nth("Vader said: No, I am your father!", 4, "a", "o")
        == "Vader said: No, I am your fother!"
    )

    assert (
        replace_nth("Vader said: No, I am your father!", 6, "a", "o")
        == "Vader said: No, I am your father!"
    )

    assert (
        replace_nth("Vader said: No, I am your father!", 0, "a", "o")
        == "Vader said: No, I am your father!"
    )

    assert (
        replace_nth("Vader said: No, I am your father!", -2, "a", "o")
        == "Vader said: No, I am your father!"
    )

    assert (
        replace_nth("Vader said: No, I am your father!", 1, "i", "y")
        == "Vader sayd: No, I am your father!"
    )

    assert (
        replace_nth("Luke cries: Noooooooooooooooo!", 6, "o", "i")
        == "Luke cries: Noooooioooooioooo!"
    )
