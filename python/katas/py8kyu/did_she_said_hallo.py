# Kata url: https://www.codewars.com/kata/56a4addbfd4a55694100001f.

def validate_hello(greetings: str) -> bool:
    greetings = greetings.lower()
    return any(
        w in greetings for w in
        ('hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc')
    )
