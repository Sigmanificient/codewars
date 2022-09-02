"""Kata url: https://www.codewars.com/kata/534eb5ad704a49dcfa000ba6."""


def hanoi(disks: int) -> int:
    return 2 ** disks - 1


def test_hanoi():
    assert hanoi(1) == 1
    assert hanoi(2) == 3
    assert hanoi(3) == 7
    assert hanoi(5) == 31
    assert hanoi(10) == 1023
    assert hanoi(20) == 1048575
