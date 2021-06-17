from datetime import datetime


def period_is_late(last: datetime, today: datetime, cycle_length: int) -> int:
    """Kata url: https://www.codewars.com/kata/578a8a01e9fd1549e50001f1."""
    return (today - last).days > cycle_length
