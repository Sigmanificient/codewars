from typing import List

week: List[str] = [
    "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
]


def whatday(num: int) -> str:
    """Kata url: https://www.codewars.com/kata/59dd3ccdded72fc78b000b25."""
    if num < 1 or num > 7:
        return "Wrong, please enter a number between 1 and 7"

    return week[num - 1]
