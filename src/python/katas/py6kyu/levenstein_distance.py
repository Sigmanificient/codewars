"""Kata url: https://www.codewars.com/kata/545cdb4f61778e52810003a2."""

def levenshtein(a,b):
    m, n = len(a) + 1, len(b) + 1
    d = [
        [(i or j) * (i == 0 or j == 0) for j in range(n)]
        for i in range(m)
    ]

    for j in range(1, n):
        for i in range(1, m):
            d[i][j] = min(
                d[i-1][j] + 1,  # deletion
                d[i][j-1] + 1,  # insertion
                d[i-1][j-1] + (a[i - 1] != b[j - 1])  # substitution
            )
    return d[m-1][n-1]