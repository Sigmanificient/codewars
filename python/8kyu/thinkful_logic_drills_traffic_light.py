lights = ['green', 'yellow', 'red']


def update_light(current: str) -> str:
    """https://www.codewars.com/kata/58649884a1659ed6cb000072"""
    return lights[(lights.index(current) + 1) % len(lights)]
