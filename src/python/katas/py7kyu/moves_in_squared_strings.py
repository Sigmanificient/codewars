"""Kata url: https://www.codewars.com/kata/56dbe0e313c2f63be4000b25."""


def vert_mirror(strng):
    return '\n'.join(
        s[::-1] for s in strng.split('\n')
    )


def hor_mirror(strng):
    return '\n'.join(
        strng.split('\n')[::-1]
    )


def oper(fct, s):
    return fct(s)


def test_oper():
    assert oper(
        vert_mirror, "hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu"
    ) == "QHdgSh\noaMDnH\nXxNNlC\nHxxvRi\nAvVTqb\nuRySvw"

    assert oper(
        vert_mirror, "IzOTWE\nkkbeCM\nWuzZxM\nvDddJw\njiJyHF\nPVHfSx"
    ) == "EWTOzI\nMCebkk\nMxZzuW\nwJddDv\nFHyJij\nxSfHVP"

    assert oper(
        hor_mirror, "lVHt\nJVhv\nCSbg\nyeCt"
    ) == "yeCt\nCSbg\nJVhv\nlVHt"

    assert oper(
        hor_mirror, "njMK\ndbrZ\nLPKo\ncEYz"
    ) == "cEYz\nLPKo\ndbrZ\nnjMK"
