"""Kata url: https://www.codewars.com/kata/5864f90473bd9c4b47000057."""

def connect_four_place(columns):
    board = [[] for _ in range(7)]

    for turn, col in enumerate(columns):
        board[col].append("YR"[turn & 1])

    final_board = [''.join(col).ljust(6, '-') for col in board]
    return [[*l] for l in zip(*final_board)][::-1]