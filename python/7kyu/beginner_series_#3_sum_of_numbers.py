def get_sum(a: int, b: int) -> int:
    """ https://www.codewars.com/kata/55f2b110f61eb01779000053

    Given two integers a and b, which can be positive or negative, find the sum of all the integers between and
    including them and return it. If the two numbers are equal return a or b.
    Note: a and b are not ordered!
    """
    if b < a:
        a, b = b, a

    return sum(range(a, b + 1))
