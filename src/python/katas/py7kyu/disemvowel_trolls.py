"""Kata url: https://www.codewars.com/kata/52fba66badcd10859f00097e."""

def disemvowel(string):
    return ''.join(char for char in string if char.lower() not in 'aeiou')
