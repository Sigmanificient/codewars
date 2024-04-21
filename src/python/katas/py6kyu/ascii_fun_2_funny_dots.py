"""Kata url: https://www.codewars.com/kata/59098c39d8d24d12b6000020."""


def dot(n: int, m: int) -> str:
    lines = ["|" + " o |" * n, "+" + "---+" * n]
    return lines[-1] + "\n" + "\n".join(lines * m)


def test_dot():
    assert dot(1, 1) == "+---+\n| o |\n+---+"

    assert dot(3, 2) == (
        "+---+---+---+\n"
        "| o | o | o |\n"
        "+---+---+---+\n"
        "| o | o | o |\n"
        "+---+---+---+"
    )