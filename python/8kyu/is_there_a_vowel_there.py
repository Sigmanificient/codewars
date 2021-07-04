def is_vow(inp):
    """Kata url: https://www.codewars.com/kata/57cff961eca260b71900008f."""
    return [chr(x) if (chr(x) if isinstance(x, int) else x) in 'aeiou' else x for x in inp]
