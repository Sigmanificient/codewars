def disemvowel(string):
    """Kata url: https://www.codewars.com/kata/52fba66badcd10859f00097e."""
    return ''.join(char for char in string if char.lower() not in 'aeiou')
