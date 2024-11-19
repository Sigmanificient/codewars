"""Kata url: https://www.codewars.com/kata/5a434a9dc5e284724f000011."""

from collections import Counter

def replace_common(st, letter):
    counts = Counter(c for c in st if c != ' ')
    replaced = max(counts, key=lambda k: counts[k])

    return st.replace(replaced, letter)