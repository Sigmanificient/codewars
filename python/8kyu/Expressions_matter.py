def expression_matter(a: int, b: int, c: int) -> int:
    """Kata url: https://www.codewars.com/kata/5ae62fcf252e66d44d00008e."""
    return max((a + b) * c, a + b * c, a * b + c, a * (b + c), a + b + c, a * b * c)
