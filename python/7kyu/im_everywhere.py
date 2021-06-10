def i(word):
    """
    https://www.codewars.com/kata/6097a9f20d32c2000d0bdb98

    Your task is to make a function that takes the value of word and returns it with an "i" at the beginning of the
    word. For example we get the word "Phone", so we must return "iPhone". But we have a few rules:

    The word should not begin with the letter "I", for example Inspire.
    The number of vowels should not be greater than or equal to the number of consonants, for example East or Peace.
    ("y" is considered a consonant)

    The first letter should not be lowercase, for example road.
    If the word does not meet the rules, we return "Invalid word".
    """
    if not word:
        return 'Invalid word'

    if word[0] == 'I' or word[0].islower():
        return 'Invalid word'

    vowels = sum(True for v in word.lower() if v in 'aeiou')

    if len(word) - vowels <= vowels:
        return 'Invalid word'

    return f"i{word}"
