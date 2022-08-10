"""Kata url: https://www.codewars.com/kata/581331293788bc1702001fa6."""


def mirror(text: str) -> str:
    lines = text[::-1].split(' ')[::-1]
    length = len(max(lines, key=len))

    content = '\n'.join(
        f"* {line:<{length}} *"
        for line in lines if line
    )

    deco = '*' * (length + 4)
    return f'{deco}\n{content}\n{deco}'


def test_mirror():
    assert mirror("Hello World") == "*********\n* olleH *\n* dlroW *\n*********"
    assert mirror("Codewars") == "************\n* srawedoC *\n************"
    assert mirror("a  b    c") == '*****\n* a *\n* b *\n* c *\n*****'
    assert mirror("emosewA !ataK") == (
        "***********\n* Awesome *\n* Kata!   *\n***********"
    )

