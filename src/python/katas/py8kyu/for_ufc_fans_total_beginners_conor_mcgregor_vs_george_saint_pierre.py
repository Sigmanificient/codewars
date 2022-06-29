"""Kata url: https://www.codewars.com/kata/582dafb611d576b745000b74."""


def quote(fighter: str) -> str:
    return (
        "I am not impressed by your performance."
        if fighter.lower() == "george saint pierre" else
        "I'd like to take this chance to apologize.. To absolutely NOBODY!"
    )


def test_quote():
    assert quote('george saint pierre') == "I am not impressed by your performance."
    assert quote('conor mcgregor') == "I'd like to take this chance to apologize.. To absolutely NOBODY!"

    assert quote('George Saint Pierre') == "I am not impressed by your performance."
    assert quote('Conor McGregor') == "I'd like to take this chance to apologize.. To absolutely NOBODY!"
