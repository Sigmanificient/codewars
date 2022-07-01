# Kata url: https://www.codewars.com/kata/56a4addbfd4a55694100001f.

def validate_hello(greetings: str) -> bool:
    greetings = greetings.lower()
    return any(
        w in greetings for w in
        ('hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc')
    )


def test_validate():
    assert validate_hello('hello')
    assert validate_hello('ciao bella!')
    assert validate_hello('salut')
    assert validate_hello('hallo, salut')
    assert validate_hello('hombre! Hola!')
    assert validate_hello('Hallo, wie geht\'s dir?')
    assert validate_hello('AHOJ!')
    assert validate_hello('czesc')
    assert not validate_hello('meh')
    assert validate_hello('Ahoj')
