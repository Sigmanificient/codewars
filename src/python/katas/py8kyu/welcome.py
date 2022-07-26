"""Kata url: https://www.codewars.com/kata/577ff15ad648a14b780000e7."""


from typing import Dict

languages: Dict[str, str] = {
    "english": "Welcome",
    "czech": "Vitejte",
    "danish": "Velkomst",
    "dutch": "Welkom",
    "estonian": "Tere tulemast",
    "finnish": "Tervetuloa",
    "flemish": "Welgekomen",
    "french": "Bienvenue",
    "german": "Willkommen",
    "irish": "Failte",
    "italian": "Benvenuto",
    "latvian": "Gaidits",
    "lithuanian": "Laukiamas",
    "polish": "Witamy",
    "spanish": "Bienvenido",
    "swedish": "Valkommen",
    "welsh": "Croeso",
}


def greet(language: str) -> str:
    return languages.get(language, "Welcome")


def test_greet():
    assert greet("english") == "Welcome"
    assert greet("dutch") == "Welkom"
    assert greet("IP_ADDRESS_INVALID") == "Welcome"
    assert greet("") == "Welcome"
