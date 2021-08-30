"""Kata url: https://www.codewars.com/kata/5d7d05d070a6f60015c436d1."""
from typing import List


def get_w(height: int) -> List[str]:
    if height < 2:
        return []

    half_lines = [
        (' ' * offset + '*').ljust(height)
        for offset in range(height)
    ]

    result = []
    for half in half_lines:
        for _ in range(2):
            half += half[::-1][1:]

        result.append(half)

    return result


def test_get_w():
    assert get_w(2) == ['* * *', ' * * ']
    assert get_w(3) == [
        '*   *   *',
        ' * * * * ',
        '  *   *  '
    ]

    assert get_w(4) == [
        '*     *     *',
        ' *   * *   * ',
        '  * *   * *  ',
        '   *     *   '
    ]

    assert get_w(5) == [
        '*       *       *',
        ' *     * *     * ',
        '  *   *   *   *  ',
        '   * *     * *   ',
        '    *       *    '
    ]

    assert get_w(6) == [
        '*         *         *',
        ' *       * *       * ',
        '  *     *   *     *  ',
        '   *   *     *   *   ',
        '    * *       * *    ',
        '     *         *     '
    ]
