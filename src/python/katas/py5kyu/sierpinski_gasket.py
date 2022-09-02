"""Kata url: https://www.codewars.com/kata/53ea3ad17b5dfe1946000278."""


def sierpinski(n):
    lines = ['L']
    length = 1

    for _ in range(n):
        buf = lines[:]

        for line in lines:
            buf.append(line.ljust(length) + ' ' + line)

        length = len(buf[-1])
        lines = buf

    return '\n'.join(lines)


def test_sierpinski():
    assert sierpinski(0) == 'L'
    assert sierpinski(1) == 'L\nL L'
    assert sierpinski(2) == 'L\nL L\nL   L\nL L L L'
    assert sierpinski(3) == (
        'L\nL L\nL   L\nL L L L\nL       L\n'
        'L L     L L\nL   L   L   L\nL L L L L L L L'
    )
