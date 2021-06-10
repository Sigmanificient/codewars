

def find_it(seq):
    """ Given an array of integers, find the one that appears an odd number of times.
    There will always be only one integer that appears an odd number of times. """
    return [x for x in set(seq) if seq.count(x) % 2][-1]
