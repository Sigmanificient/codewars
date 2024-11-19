"""Kata url: https://www.codewars.com/kata/588417e576933b0ec9000045."""

def seats_in_theater(tot_cols, tot_rows, col, row):
    return (tot_cols - col + 1) * (tot_rows - row)