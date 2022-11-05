"""Kata url: https://www.codewars.com/kata/587c0138110b20624e000253."""


def interpreter(tape, array):
    array = list(map(int, array))
    end, prog_end = len(array), len(tape)
    cursor = ins = 0

    while cursor < end:
        if tape[ins % prog_end] == '0':
            cursor += 1
        else:
            array[cursor] ^= 1
        ins += 1
    return ''.join(map(str, array))


def test_interpreter():
    assert interpreter('10', '1100101') == '0011010'
    assert interpreter('100', '1111111111') == '0101010101'
