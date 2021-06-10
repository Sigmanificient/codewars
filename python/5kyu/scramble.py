def scramble(s1: str, s2: str) -> bool:
    """
    https://www.codewars.com/kata/55c04b4cc56a697bb0000048

    Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to
    match str2, otherwise returns false.
    """
    return all(s1.count(x) >= s2.count(x) for x in sorted(set(s2)))
