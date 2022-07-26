"""Kata url: https://www.codewars.com/kata/59df2f8f08c6cec835000012."""


def meeting(s: str) -> str:
    return "".join(
        f"({', '.join(name)})"
        for name in sorted(x.split(":")[::-1] for x in s.upper().split(";"))
    )


def test_meeting():
    assert meeting(
        "Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;"
        "Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn"
    ) == (
        "(ARNO, ANN)(BELL, JOHN)(CORNWELL, ALEX)(DORNY, ABBA)(KERN, LEWIS)(KORN"
        ", ALEX)(META, GRACE)(SCHWARZ, VICTORIA)(STAN, MADISON)(STAN, MEGAN)(WA"
        "HL, ALEXIS)"
    )

    assert meeting(
        "John:Gates;Michael:Wahl;Megan:Bell;Paul:Dorries;James:Dorny;Lewis:Stev"
        "e;Alex:Meta;Elizabeth:Russel;Anna:Korn;Ann:Kern;Amber:Cornwell"
    ) == (
        "(BELL, MEGAN)(CORNWELL, AMBER)(DORNY, JAMES)(DORRIES, PAUL)(GATES, JOH"
        "N)(KERN, ANN)(KORN, ANNA)(META, ALEX)(RUSSEL, ELIZABETH)(STEVE, LEWIS)"
        "(WAHL, MICHAEL)"
    )

    assert meeting(
        "Alex:Arno;Alissa:Cornwell;Sarah:Bell;Andrew:Dorries;Ann:Kern;Haley:Arn"
        "o;Paul:Dorny;Madison:Kern"
    ) == (
        "(ARNO, ALEX)(ARNO, HALEY)(BELL, SARAH)(CORNWELL, ALISSA)(DORNY, PAUL)("
        "DORRIES, ANDREW)(KERN, ANN)(KERN, MADISON)"
    )
