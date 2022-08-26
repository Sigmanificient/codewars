"""Kata url: https://www.codewars.com/kata/595ddfe2fc339d8a7d000089."""
ALPHA = "abcdefghijklmnopqrstuvwxyz"


def hamster_me(code, message):
    char_values: list[int] = [0] * 26

    for letter in set(code):
        char_values[ALPHA.index(letter)] = 1

    char = ''
    x = 0

    for i in range(26):
        item = char_values[i]

        if item == 1:
            char = ALPHA[i]
            x = 0

        x += 1
        char_values[i] = f'{char}{x}'

    char_values: list[str]
    for i in range(26):
        item = char_values[i]
        x += 1

        if item.isdigit():
            char_values[i] = f'{char}{x}'

    trans = {k: v for k, v in zip(ALPHA, char_values)}
    return ''.join(trans[letter] for letter in message)


def test_hamster_me():
    assert hamster_me("hamster", "hamster") == "h1a1m1s1t1e1r1"
    assert hamster_me("hamster", "helpme") == "h1e1h5m4m1e1"
    assert hamster_me("hmster", "hamster") == "h1t8m1s1t1e1r1"
    assert hamster_me("hhhhammmstteree", "hamster") == "h1a1m1s1t1e1r1"
    assert hamster_me(
        "hamster", "abcdefghijklmnopqrstuvwxyz"
    ) == "a1a2a3a4e1e2e3h1h2h3h4h5m1m2m3m4m5r1s1t1t2t3t4t5t6t7"

    assert hamster_me(
        "f", "abcdefghijklmnopqrstuvwxyz"
    ) == (
        "f22f23f24f25f26f1f2f3f4f5f6f7f8f9f10f11f12f13f14f15f16f17f18f19f20f21"
    )
