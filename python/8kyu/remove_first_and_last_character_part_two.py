# Kata url: https://www.codewars.com/kata/570597e258b58f6edc00230d.

def array(string: str) -> str:
    return ' '.join(string.split(',')[1:-1]) or None
