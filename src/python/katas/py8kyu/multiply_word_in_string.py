"""Kata url: https://www.codewars.com/kata/5ace2d9f307eb29430000092."""


def modify_multiply(st: str, loc: int, num: int) -> str:
    return '-'.join(st.split(' ')[loc] for _ in range(num))


def test_modify_multiply():
    assert modify_multiply(
        "This is a string", 3, 5
    ) == "string-string-string-string-string"

    assert modify_multiply(
        "Creativity is the process of having original ideas that have value."
        " It is a process; it's not random.", 8, 10
    ) == "that-that-that-that-that-that-that-that-that-that"

    assert modify_multiply(
        "Self-control means wanting to be effective at some random point"
        " in the infinite radiations of my spiritual existence",
        1, 1
    ) == "means"

    assert modify_multiply(
        "Is sloppiness in code caused by ignorance or apathy? "
        "I don't know and I don't care.", 6, 8
    ) == (
        "ignorance-ignorance-ignorance-ignorance"
        "-ignorance-ignorance-ignorance-ignorance"
    )

    assert modify_multiply(
        "Everything happening around me is very random. "
        "I am enjoying the phase, as the journey is far more enjoyable "
        "than the destination.", 2, 5
    ) == "around-around-around-around-around"
