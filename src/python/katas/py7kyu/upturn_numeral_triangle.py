"""Kata url: https://www.codewars.com/kata/564f3d49a06556d27c000077."""


def pattern(n: int) -> str:
    return '\n'.join(
        (' ' * i) + ' '.join(str(i % 10) * ((n + 1) - i))
        for i in range(1, n + 1)
    )


def test_pattern():
    assert pattern(7) == (
        " 1 1 1 1 1 1 1\n"
        "  2 2 2 2 2 2\n"
        "   3 3 3 3 3\n"
        "    4 4 4 4\n"
        "     5 5 5\n"
        "      6 6\n"
        "       7"
    )

    assert pattern(12) == (
        " 1 1 1 1 1 1 1 1 1 1 1 1\n"
        "  2 2 2 2 2 2 2 2 2 2 2\n"
        "   3 3 3 3 3 3 3 3 3 3\n"
        "    4 4 4 4 4 4 4 4 4\n"
        "     5 5 5 5 5 5 5 5\n"
        "      6 6 6 6 6 6 6\n"
        "       7 7 7 7 7 7\n"
        "        8 8 8 8 8\n"
        "         9 9 9 9\n"
        "          0 0 0\n"
        "           1 1\n"
        "            2"
    )

    assert pattern(21) == (
        " 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1\n"
        "  2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2\n"
        "   3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3\n"
        "    4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4\n"
        "     5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5\n"
        "      6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6\n"
        "       7 7 7 7 7 7 7 7 7 7 7 7 7 7 7\n"
        "        8 8 8 8 8 8 8 8 8 8 8 8 8 8\n"
        "         9 9 9 9 9 9 9 9 9 9 9 9 9\n"
        "          0 0 0 0 0 0 0 0 0 0 0 0\n"
        "           1 1 1 1 1 1 1 1 1 1 1\n"
        "            2 2 2 2 2 2 2 2 2 2\n"
        "             3 3 3 3 3 3 3 3 3\n"
        "              4 4 4 4 4 4 4 4\n"
        "               5 5 5 5 5 5 5\n"
        "                6 6 6 6 6 6\n"
        "                 7 7 7 7 7\n"
        "                  8 8 8 8\n"
        "                   9 9 9\n"
        "                    0 0\n"
        "                     1"
    )
