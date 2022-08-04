"""Kata url: https://www.codewars.com/kata/5fc7d2d2682ff3000e1a3fbc."""


def is_a_valid_message(message: str) -> bool:
    if not message:
        return True

    items = []
    word = ""
    digits = True

    for char in message:
        is_digits = char.isdigit()
        if is_digits != digits:
            digits = not digits
            items.append(word)
            word = ""
        word += char

    items.append(word)

    if len(items) % 2:
        return False

    for num, word in zip(items[::2], items[1::2]):
        if not num:
            return False

        if int(num) != len(word):
            return False

    return True


def test_is_a_valid_message():
    assert is_a_valid_message("3hey5hello2hi")
    assert is_a_valid_message("4code13hellocodewars")
    assert is_a_valid_message("1a2bb3ccc4dddd5eeeee")
    assert is_a_valid_message("")

    assert not is_a_valid_message("3hey5hello2hi5")
    assert not is_a_valid_message("code4hello5")
