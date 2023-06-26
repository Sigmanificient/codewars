"""Kata url: https://www.codewars.com/kata/59bf6b73bf10a4c8e5000047a."""

from string import ascii_lowercase


def get_key(key):
    new_key = ''

    for k in key + ascii_lowercase:
        if k not in new_key:
            new_key += k
    return new_key


def cipher(func):
    def wrapper(message, key, shift):
        key = get_key(key)
        output = ''

        for c in message:
            index = key.find(c)
            if index == -1:
                output += c
                continue
            encoded_char, shift = func(key, shift, index)
            output += encoded_char
        return output
    return wrapper


@cipher
def encode(key, shift, index):
    return key[(index + shift) % 26], index + 1


@cipher
def decode(key, shift, index):
    d = key[index - shift % 26]
    return d, (key.find(d) + 1)
