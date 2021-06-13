def count_sheeps(sheep):
    """Kata url: https://www.codewars.com/kata/54edbc7200b811e956000556."""
    return sum(x for x in sheep if isinstance(x, bool))
