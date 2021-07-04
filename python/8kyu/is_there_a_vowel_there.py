def is_vow(inp):
    return [chr(x) if (chr(x) if isinstance(x, int) else x) in 'aeiou' else x for x in inp]
