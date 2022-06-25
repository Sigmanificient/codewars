def to_camel_case(text: str) -> str:
    return ''.join(
        w.capitalize() if c else w
        for c, w in enumerate(
            text.replace('_', '-').split('-')
        )
    )


def test_to_camel_case():
    assert to_camel_case('') == ''
    assert to_camel_case("the_stealth_warrior") == "theStealthWarrior"
    assert to_camel_case("The-Stealth-Warrior") == "TheStealthWarrior"
    assert to_camel_case("A-B-C") == "ABC"
