def how_much_i_love_you(nb_petals):
    """Kata url: https://www.codewars.com/kata/57f24e6a18e9fad8eb000296."""
    return ("I love you", "a little", "a lot", "passionately", "madly", "not at all")[(nb_petals - 1) % 6]
