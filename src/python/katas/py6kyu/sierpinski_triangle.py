"""Kata url: https://www.codewars.com/kata/58add662ea140541a50000f7."""


def sierpinski(n):
    lines = ['*']
    length = 1

    for _ in range(n):
        buf = lines[:]

        for line in lines:
            buf.append(line.ljust(length) + ' ' + line)

        length = len(buf[-1])
        lines = buf

    return '\n'.join(line.center(length) for line in lines)


def test_sierpinski():
    assert sierpinski(1) == ' * \n* *'
    assert sierpinski(2) == '   *   \n  * *  \n *   * \n* * * *'
    assert sierpinski(3) == (
        '       *       \n'
        '      * *      \n'
        '     *   *     \n'
        '    * * * *    \n'
        '   *       *   \n'
        '  * *     * *  \n'
        ' *   *   *   * \n'
        '* * * * * * * *'
    )
