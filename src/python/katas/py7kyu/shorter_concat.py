"""Kata url: https://www.codewars.com/kata/54557d61126a00423b000a45."""

def shorter_reverse_longer(a, b):
    if len(a) >= len(b):
        a, b = b, a
    return f"{a}{b[::-1]}{a}"


def test_shorter_reverse_longer():
    assert shorter_reverse_longer("first", "abcde") == "abcdetsrifabcde"
    assert shorter_reverse_longer("hello", "bau") == "bauollehbau"
    assert shorter_reverse_longer("abcde", "fghi") == "fghiedcbafghi"
