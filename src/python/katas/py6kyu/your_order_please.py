"""Kata url: https://www.codewars.com/kata/55c45be3b2079eccff00010f."""


def order(sentence: str) -> str:
    return ' '.join(
        sorted(
            sentence.split(' '),
            key=lambda s: ''.join(x for x in s if x.isdigit())
        )
    )


def test_order():
    assert order("") == ""
    assert order("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est"
    assert order("4of Fo1r pe6ople g3ood th5e the2") == "Fo1r the2 g3ood 4of th5e pe6ople"
