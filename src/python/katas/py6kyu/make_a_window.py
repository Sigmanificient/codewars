"""Kata url: https://www.codewars.com/kata/59c03f175fb13337df00002e."""


def make_a_window(num: int) -> str:
    glass = ('|' + ('.' * num)) * 2 + '|'
    window = (
        [base := '-' * ((2 * num) + 3)],
        [glass for _ in range(num)],
        ['|' + ('-' * num) + '+' + ('-' * num) + '|'],
        [glass for _ in range(num)],
        [base]
    )

    return '\n'.join(sum(window, []))


def test_make_a_window():
    assert make_a_window(3) == (
        "---------\n"
        "|...|...|\n"
        "|...|...|\n"
        "|...|...|\n"
        "|---+---|\n"
        "|...|...|\n"
        "|...|...|\n"
        "|...|...|\n"
        "---------"
    )

    assert make_a_window(2) == (
        "-------\n"
        "|..|..|\n"
        "|..|..|\n"
        "|--+--|\n"
        "|..|..|\n"
        "|..|..|\n"
        "-------"
    )

    assert make_a_window(1) == (
        "-----\n"
        "|.|.|\n"
        "|-+-|\n"
        "|.|.|\n"
        "-----"
    )
