"""Kata url: https://www.codewars.com/kata/57e8fba2f11c647abc000944."""


def fire_fight(s: str) -> str:
    return s.replace('Fire', '~~')


def test_fire_fight():
    assert fire_fight('Fire') == '~~'
    assert fire_fight(
        "Boat Rudder Mast Boat Hull Water Fire Boat Deck Hull Fire Propeller "
        "Deck Fire Deck Boat Mast"
    ) == (
        "Boat Rudder Mast Boat Hull Water ~~ Boat Deck Hull ~~ Propeller Deck "
        "~~ Deck Boat Mast"
    )

    assert fire_fight(
        "Mast Deck Engine Water Fire"
    ) == "Mast Deck Engine Water ~~"

    assert fire_fight(
        "Fire Deck Engine Sail Deck Fire Fire Fire Rudder Fire Boat Fire Fire "
        "Captain"
    ) == (
        "~~ Deck Engine Sail Deck ~~ ~~ ~~ Rudder ~~ Boat ~~ ~~ Captain"
    )
