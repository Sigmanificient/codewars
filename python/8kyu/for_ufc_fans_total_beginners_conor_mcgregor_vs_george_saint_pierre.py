# Kata url: https://www.codewars.com/kata/582dafb611d576b745000b74

def quote(fighter: str) -> str:
    return (
        "I am not impressed by your performance."
        if fighter.lower() == "george saint pierre" else
        "I'd like to take this chance to apologize.. To absolutely NOBODY!"
    )
