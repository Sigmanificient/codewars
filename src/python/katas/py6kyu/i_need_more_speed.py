"""Kata url: https://www.codewars.com/kata/55de9c184bb732a87f000055. """

def reverse(seq):
    size = len(seq)
    for i in range(size >> 1):
        seq[i], seq[size - i - 1] = seq[size - i - 1], seq[i]