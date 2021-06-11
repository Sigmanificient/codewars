

def find_it(seq):
    """Kata url: https://www.codewars.com/kata/54da5a58ea159efa38000836."""
    return [x for x in set(seq) if seq.count(x) % 2][-1]
