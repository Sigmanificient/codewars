"""Kata url: https://www.codewars.com/kata/5a4e3782880385ba68000018."""

BALANCED_TEXT = "Balanced"
NOT_BALANCED_TEXT = f"Not {BALANCED_TEXT}"



def balanced_num(number: int) -> str:
    n_str = str(number)
    half = len(n_str) // 2
    odd_length = not len(n_str) % 2

    return (
        "Not "
        * (
            sum(map(int, n_str[: half - odd_length]))
            != sum(map(int, n_str[half + 1 :]))
        )
        + BALANCED_TEXT
    )


def test_balanced_num():
    assert balanced_num(7) == BALANCED_TEXT
    assert balanced_num(959) == BALANCED_TEXT
    assert balanced_num(13) == BALANCED_TEXT
    assert balanced_num(432) == NOT_BALANCED_TEXT
    assert balanced_num(424) == BALANCED_TEXT

    assert balanced_num(1024) == NOT_BALANCED_TEXT
    assert balanced_num(66545) == NOT_BALANCED_TEXT
    assert balanced_num(295591) == NOT_BALANCED_TEXT
    assert balanced_num(1230987) == NOT_BALANCED_TEXT
    assert balanced_num(56239814) == BALANCED_TEXT