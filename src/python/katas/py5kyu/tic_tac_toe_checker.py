"""Kata url: https://www.codewars.com/kata/62e8608316d2d623d37ae4c4."""
from typing import List

Board = List[List[int]]


def is_solved(board: Board) -> bool:
    for line in board:
        if len(set(line)) == 1 and line[0] > 0:
            return line[0]

    for col in zip(*board):
        if len(set(col)) == 1 and col[0] > 0:
            return col[0]

    if mid := board[1][1]:
        if mid == board[0][0] == board[2][2]:
            return mid

        if mid == board[0][2] == board[2][0]:
            return mid

    zeros = min(min(line) for line in board) == 0
    return 0 - zeros


def test_is_solved():
    assert is_solved([[1, 1, 1], [0, 2, 2], [0, 0, 0]]) == 1
    assert is_solved([[1, 2, 0], [0, 1, 2], [0, 0, 1]]) == 1
    assert is_solved([[2, 1, 1], [0, 1, 1], [2, 2, 2]]) == 2
    assert is_solved([[2, 2, 2], [0, 1, 1], [1, 0, 0]]) == 2
    assert is_solved([[2, 1, 2], [2, 1, 1], [1, 2, 1]]) == 0
    assert is_solved([[1, 2, 1], [1, 1, 2], [2, 1, 2]]) == 0
    assert is_solved([[2, 0, 2], [2, 1, 1], [1, 2, 1]]) == -1
    assert is_solved([[0, 0, 2], [0, 0, 0], [1, 0, 1]]) == -1
    assert is_solved([[1, 2, 1], [1, 1, 2], [2, 2, 0]]) == -1
    assert is_solved([[0, 1, 1], [2, 0, 2], [2, 1, 0]]) == -1
