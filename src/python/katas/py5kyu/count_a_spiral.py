"""Kata url: https://www.codewars.com/kata/61559bc4ead5b1004f1aba83."""


def spiral_sum(size: int) -> int:
    return (size ** 2) // 2 + size - 1 + (size % 2)


def test_spiral():
    assert spiral_sum(5) == 17
    assert spiral_sum(10) == 59
    assert spiral_sum(1000) == 500999
    assert spiral_sum(123456) == 7620815423
    assert spiral_sum(584757902734057049235907840235937429075234) == int(
        "17097090240496646232892004748818196959669016623497609237764012"
        "1561715772973645152611"
    )
