"""Kata url: https://www.codewars.com/kata/5596700a386158e3aa000011."""


def binary_pyramid(m, n):
    s = sum(int(f'{i:b}') for i in range(m, n + 1))
    return f'{s:b}'


def test_binary_pyramid():
    assert binary_pyramid(1, 4) == "1111010"
    assert binary_pyramid(1, 6) == "101001101"
    assert binary_pyramid(6, 20) == "1110010110100011"
    assert binary_pyramid(21, 60) == "1100000100010001010100"
    assert binary_pyramid(100, 100) == "100001100100101000100"
    assert binary_pyramid(1, 1) == "1"
    assert binary_pyramid(0, 1) == "1"
    assert binary_pyramid(0, 0) == "0"
    assert binary_pyramid(1, 100) == "10011101010010110000101010"
    assert binary_pyramid(100, 1000) == (
        "111111001111110110011011000101110101110"
    )
