"""Kata url: https://www.codewars.com/kata/526d84b98f428f14a60008da."""


def hamming(n: int) -> int:
    hamming_numbers = [0] * n
    hamming_numbers[0] = 1

    a = b = c = 0
    m2, m3, m5 = 2, 3, 5

    for i in range(1, n):
        v = min(m2, m3, m5)
        hamming_numbers[i] = v

        if v == m2:
            a += 1
            m2 = hamming_numbers[a] * 2

        if v == m3:
            b += 1
            m3 = hamming_numbers[b] * 3

        if v == m5:
            c += 1
            m5 = hamming_numbers[c] * 5

    return hamming_numbers[-1]


def test_hamming():
    assert hamming(1) == 1
    assert hamming(2) == 2
    assert hamming(3) == 3
    assert hamming(4) == 4
    assert hamming(5) == 5
    assert hamming(6) == 6
    assert hamming(7) == 8
    assert hamming(8) == 9
    assert hamming(9) == 10
    assert hamming(10) == 12
    assert hamming(11) == 15
    assert hamming(12) == 16
    assert hamming(13) == 18
    assert hamming(14) == 20
    assert hamming(15) == 24
    assert hamming(16) == 25
    assert hamming(17) == 27
    assert hamming(18) == 30
    assert hamming(19) == 32
